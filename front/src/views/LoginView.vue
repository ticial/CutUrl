<script>
import InputBlock from '../components/InputBlock.vue'
import MessageList from '../components/MessageList.vue'
import axios from 'axios'

export default {
    name: 'LoginView',
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
                    hint: null,
                },
                password: {
                    value: '',
                    title: 'Пароль',
                    type: 'password',
                    name: 'password',
                    placeholder: 'Введите пароль',
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
            const formData = {
                username: this.fields.username.value,
                password: this.fields.password.value,
            }

            axios.post('/api/v1/token/login', formData)
                .then(response => {
                    this.$store.commit("login", response.data.auth_token)
                    this.$router.push({ name: 'profile' })
                    this.globalMessage('Вы успешно вошли в аккаунт', 'success')
                })
                .catch(error => {
                    let res_errors = JSON.parse(error.request.response)
                    for (let key in res_errors) {
                        this.fields[key].errors = res_errors[key]
                    }
                })
        }
    }
}
</script>

<template>
    <main>
        <p v-if="$store.state.isAuthenticated" class="center">Вы уже авторизованы. <RouterLink to="/profile"
                class="hover-underline">Перейти в профиль?</RouterLink>
        </p>
        <form v-else @submit.prevent="submitForm" class="centered-container-flex">
            <h2 class="center">Вход</h2>
            <InputBlock :field="fields.username"></InputBlock>

            <InputBlock :field="fields.password"></InputBlock>

            <MessageList :input_msgs="fields.non_field_errors.errors" :type="'error'" :time="2000" class="mt-3">
            </MessageList>

            <button type="submit" class="mt-2">Войти</button>

            <p class="center mt-4">Еще не зарегистрированы? <RouterLink to="/register" class="hover-underline">Регистрация
                </RouterLink>
            </p>

        </form>
    </main>
</template>

<style scoped></style>