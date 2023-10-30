import { createStore } from 'vuex'
import axios from 'axios'

// здесь сохраняем токен авторизации
const store = createStore({
    state: {
        isAuthenticated: false,
        token: ''
    },
    mutations: {
        login(state, token) {
            state.isAuthenticated = true
            state.token = token
            localStorage.setItem("token", token)
            axios.defaults.headers.common['Authorization'] = "Token " + token
        },
        logout(state) {
            state.isAuthenticated = false
            state.token = ''
            localStorage.removeItem("token")
            axios.defaults.headers.common['Authorization'] = ""
        },
    },
    actions: {
        onStart(context) {
            let token = localStorage.getItem("token")
            if (token) {
                axios.defaults.headers.common['Authorization'] = "Token " + token
                axios
                    .get('/api/v1/users/me/')
                    .then(response => {
                        context.commit('login', token)
                    })
                    .catch(error => {
                        context.commit('logout')
                    })
            } else {
                context.commit('logout')
            }
        }
    },
})

export default store