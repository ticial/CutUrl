<script>
import InputBlock from '../components/InputBlock.vue'
import MessageList from '../components/MessageList.vue'
import axios from 'axios'

export default {
    name: 'RegisterView',
    props: ['globalMessage'],
    data() {
        return {
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
                password: {
                    value: '',
                    title: 'Пароль',
                    type: 'password',
                    name: 'password',
                    placeholder: 'Введите пароль',
                    errors: null,
                    hint: [
                        'Ваш пароль не должен совпадать с вашим именем или другой персональной информацией или быть слишком похожим на неё.',
                        'Ваш пароль должен содержать как минимум 8 символов.',
                        'Ваш пароль не может быть одним из широко распространённых паролей.',
                        'Ваш пароль не может состоять только из цифр.',
                    ],
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
            if (this.fields.username.value === '') {
                this.fields.username.errors = ['Это поле не может быть пустым.']
                error = true
            }
            if (this.fields.email.value === '') {
                this.fields.email.errors = ['Это поле не может быть пустым.']
                error = true
            }
            if (this.fields.password.value === '') {
                this.fields.password.errors = ['Это поле не может быть пустым.']
                error = true
            }
            if (error) return

            const formData = {
                username: this.fields.username.value,
                email: this.fields.email.value,
                password: this.fields.password.value,
            }

            axios.post('/api/v1/users/', formData)
                .then(response => {
                    this.$router.push({ name: 'login' })
                    this.globalMessage('Регистрация прошла успешно!', 'success')
                })
                .catch(error => {
                    let res_errors = JSON.parse(error.request.response)
                    for (let key in res_errors) {
                        this.fields[key].errors = res_errors[key]
                    }
                })
        },
    },
}
</script>

<template>
    <main>
        <p v-if="$store.state.isAuthenticated" class="center">Вы уже зарегистрированы. <RouterLink to="/profile"
                class="hover-underline">Перейти в профиль?</RouterLink>
        </p>
        <form v-else @submit.prevent="submitForm" class="centered-container-flex">
            <h2 class="center">Регистрация</h2>

            <InputBlock :field="fields.username"></InputBlock>

            <InputBlock :field="fields.email"></InputBlock>

            <InputBlock :field="fields.password"></InputBlock>

            <MessageList :input_msgs="fields.non_field_errors.errors" :type="'error'" :time="2000" class="mt-3">
            </MessageList>

            <button type="submit" class="mt-2">Зарегистрироваться</button>

            <p class="center mt-4">Уже зарегистрированы? <RouterLink to="/login" class="hover-underline">Войти</RouterLink>
            </p>
        </form>
    </main>
</template>

<style scoped></style>