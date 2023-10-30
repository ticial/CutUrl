<script>
import InputBlock from '../components/InputBlock'
import LinkList from '../components/LinkList'
import axios from 'axios'

export default {
    name: 'LinksView',
    props: ['globalMessage'],
    data() {
        return {
            baseURL: axios.defaults.baseURL + '$',
            fields: {
                original_link: {
                    value: '',
                    title: 'Ссылка',
                    type: 'url',
                    name: 'original_link',
                    placeholder: 'Введите оригинальную сслыку',
                    errors: null,
                    hint: null,
                },
                pseudo_link: {
                    value: '',
                    title: axios.defaults.baseURL + '$',
                    type: 'text',
                    name: 'pseudo_link',
                    placeholder: 'Введите псевдоним ссылки',
                    errors: null,
                    hint: null,
                },
                non_field_errors: {
                    errors: null
                }
            },
        }
    },
    components: { InputBlock, LinkList },
    methods: {
        submitForm() {
            this.fields.non_field_errors.errors = null
            if (this.fields.original_link.value === this.original_link &&
                this.fields.pseudo_link.value === this.pseudo_link) return

            const formData = {
                original_link: this.fields.original_link.value.trim(),
                pseudo_link: this.fields.pseudo_link.value.trim(),
            }

            axios.post('/api/link-create', formData)
                .then(response => {
                    // console.log('Success', response)
                    this.$refs.LinkList.getLinks()
                    this.fields.original_link.value = ''
                    this.fields.pseudo_link.value = ''
                    this.globalMessage('Ссылка успешно создана!', 'success')
                    setTimeout(() => this.success_message = false, 2000)
                })
                .catch((error) => {
                    console.log('Error', error)
                    if (error.request.statusText === 'Unauthorized') {
                        return
                    }
                    const res_errors = JSON.parse(error.request.response)
                    for (let key in res_errors) {
                        this.fields[key].errors = res_errors[key]
                    }
                })
        },
    }
}
</script>

<template>
    <main>
        <p v-if="!$store.state.isAuthenticated" class="center">Только авторизованные пользователи могут сокращать
                ссылки. <RouterLink to="/login" class="hover-underline">Войти?</RouterLink>
        </p>
        <form v-else class="centered-container-flex">
            <h2 class="center">Сократитель ссылок</h2>

            <InputBlock :field="fields.original_link"></InputBlock>

            <InputBlock :field="fields.pseudo_link"></InputBlock>
            
            <button type="button" @click="submitForm" class="mt-4">Создать</button>
        </form>
        <LinkList v-if="$store.state.isAuthenticated" ref="LinkList" :baseURL="baseURL"></LinkList>
        
    </main>
</template>
