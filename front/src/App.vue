<script>
import { RouterView } from 'vue-router'
import Header from './components/Header.vue'
import Footer from './components/Footer.vue'
import MessageList from './components/MessageList.vue'
import axios from 'axios'

export default {
    name: 'App',
    components: { Header, Footer, MessageList },
    data() {
        return {}
    },
    watch: {
        $route() {
            this.$store.dispatch("onStart")
        }
    },
    methods: {
        logout() {
            axios.post('/api/v1/token/logout')
                .then(response => {
                    console.log('Success', response)
                    this.$store.commit("logout")
                    this.$router.push({ name: 'home' })
                    this.globalMessage('Вы вышли из аккаунта', 'success')
                })
                .catch(error => {
                    console.log('Error', error)
                }) 
        },
        globalMessage(text, type, time=2000){
            this.$refs.messages.addMessage(text, type, time)
        },
    }
}
</script>

<template>
    <main class="wrapper">
        <Header :logout="logout"></Header>
        <div class="content">
            <MessageList ref="messages" class="global-message-block"></MessageList>
            <RouterView :logout="logout" :globalMessage="globalMessage" class="mt-10"/>
        </div>
        <Footer></Footer>
    </main>
</template>

<style scoped>

.global-message-block {
    min-height: 50px;
}

</style>
