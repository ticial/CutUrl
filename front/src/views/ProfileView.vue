<script>
import InputBlock from '../components/InputBlock.vue'
import MessageList from '../components/MessageList.vue'
import axios from 'axios'

export default {
    name: 'ProfileView',
    props: ['logout', 'globalMessage'],
    data() {
        return {
            username: '',
            email: '',
            fields: {
                username: {
                    value: '',
                    title: 'Имя',
                    type: 'text',
                    name: 'username',
                    placeholder: 'Введите имя',
                    errors: null,
                    hint: ['Не более 150 символов. Только буквы, цифры и символы @/./+/-/_.'],
                },
                email: {
                    value: '',
                    title: 'Email',
                    type: 'email',
                    name: 'email',
                    placeholder: 'Введите email',
                    errors: null,
                    hint: null,
                },
                non_field_errors: {
                    errors: null
                }
            },
        }
    },
    components: { InputBlock, MessageList },
    methods: {
        submitForm(e) {
            let error = false
            if (this.fields.username.value === ''){
                this.fields.username.errors = ['Это поле не может быть пустым.']
                error = true
            }
            if (this.fields.email.value === ''){
                this.fields.email.errors = ['Это поле не может быть пустым.']
                error = true
            }
            if (error) return
            if (this.fields.username.value === this.username &&
                this.fields.email.value === this.email) return
            
            const formData = {
                username: this.fields.username.value,
                email: this.fields.email.value,
            }

            axios.put('/api/user-update', formData)
                .then(response => {
                    this.getUserData()
                    this.globalMessage('Данные профиля обновлены!', 'success')
                })
                .catch((error) => {
                    const res_errors = JSON.parse(error.request.response)
                    for (let key in res_errors) {
                        this.fields[key].errors = res_errors[key]
                    }
                })
        },
        getUserData() {
            axios
                .get('/api/v1/users/me/')
                .then(response => {
                    this.username = response.data.username
                    this.fields.username.value = response.data.username
                    this.email = response.data.email
                    this.fields.email.value = response.data.email
                })
                .catch(error => {
                    this.$store.commit("logout")
                    this.$router.push({ name: 'login' })
                })
        },
        undoForm() {
            this.fields.username.value = this.username
            this.fields.email.value = this.email
        }
    },
    mounted() {
        this.getUserData()
    }
}
</script>

<template>
    <main>
        <div class="centered-container-flex">
            <h2 class="center">Кабинет пользователя</h2>
            <div class="hint-block mt-4">
                <p class="center"><b>@{{ username }}</b></p>
                <p class="center mt-2"><b>Email: </b>{{ email }}</p>
            </div>
            <button type="button" @click="logout()" class="shadow-hover mt-2">Выйти</button>
        </div>

        <form @submit.prevent="submitForm" class="centered-container-flex mt-5">
            <h2 class="center">Изменить данные</h2>

            <InputBlock :field="fields.username"></InputBlock>

            <InputBlock :field="fields.email"></InputBlock>

            <MessageList :input_msgs="fields.non_field_errors.errors" :type="'error'" :time="2000" class="mt-3"></MessageList>
            
            <div class="button-group mt-2">
                <button type="submit">Сохранить</button>
                <button type="button" @click="undoForm()">Отменить</button>
            </div>
        </form>
    </main>
</template>

