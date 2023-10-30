<script>
import InputBlock from '../components/InputBlock.vue'
import axios from 'axios'

export default {
    name: 'LinkList',
    props: ['baseURL'],
    data() {
        return {
            link_list: [],
            mouse_coord: {
                x: 0,
                y: 0,
            },
        }
    },
    components: { InputBlock },
    methods: {
        getLinks() {
            if (!this.$store.state.isAuthenticated) return
            axios
                .get('/api/links/?format=json')
                .then(response => {
                    // console.log('getLinks() Success', response)
                    this.link_list = response.data
                })
                .catch(error => {
                    console.log(error)
                    // console.log('getLinks() Error', error)
                })
        },
        removeLink(link) {
            const confirmed = confirm('Действительно хотите удалить ссылку?\n' + this.shortLink(link))
            if (!confirmed) return
            axios
                .delete('/api/link-remove/' + link.pseudo_link)
                .then(response => {
                    // console.log('removeLink() Success', response)
                    this.getLinks()
                })
                .catch(error => {
                    console.log(error)
                    // console.log('removeLink() Error', error)
                })
        },
        shortLink(link) {
            return this.baseURL + link.pseudo_link
        },
        copyLink(link_text) {
            // костыли для копирования по клику
            const copyTextarea = document.createElement('textarea')
            copyTextarea.value = link_text
            document.body.appendChild(copyTextarea)
            copyTextarea.select()
            try {
                var successful = document.execCommand('copy')
                // console.log(successful ? 'Скопировано' : 'Не скопировано')
                this.contextMessage('Скопировано')
            } catch (err) {
                console.err('Ошибка при копировании:' + err);
            } finally {
                document.body.removeChild(copyTextarea)
            }
        },
        contextMessage(text){
            // сообщение у курсора
            const msg = this.$refs.ctx_message
            msg.innerText = text
            // console.log(this.mouse_coord);
            msg.style.display = 'block'
            msg.style.left = this.mouse_coord.x + 10 +'px'
            msg.style.top = this.mouse_coord.y + 15 + 'px'
            setTimeout(() => {
                msg.innerText = ''
                msg.style.display = 'none'
            }, 1000)
        },
        setEventCoord(e){
            this.mouse_coord.x = e.clientX
            this.mouse_coord.y = e.clientY
        },
    },
    created: function () {
        document.addEventListener('mousemove', this.setEventCoord)
    },
    destroyed: function () {
        document.removeEventListener('mousemove', this.setEventCoord)
    },
    mounted() {
        this.getLinks()
    },
}
</script>


<template>
    <div v-if="link_list.length > 0" class="centered-container-flex mt-5">
        <h2 class="center">Ваши ссылки</h2>
        <div v-for="el in link_list" :key="el.id" class="link-block mt-3">
            <div class="top-row" title="Копировать" @click="copyLink(shortLink(el))">
                <span>Ссылка:&nbsp;
                    <a :href="shortLink(el)" title="Перейти">{{ shortLink(el) }}</a>
                </span>
                <div>
                    <span title="Переходы"><img src="/img/earth-americas-solid.svg" alt="Переходы:">{{ el.redirect_count
                    }}</span>
                    <button type="button" @click="removeLink(el)"><img src="/img/xmark-solid.svg" alt="Удалить"
                            title="Удалить"></button>
                </div>
            </div>
            <p class="bottom-row">Оригинал:&nbsp;
                <a :href="el.original_link">{{ el.original_link }}</a>
            </p>
        </div>
        <div id="ctx-message" ref="ctx_message"></div>
    </div>
    
</template>

<style scoped>

.link-block {
    background: var(--silver1-color);
    border: 2px solid var(--silver1-color);
    border-radius: 20px;
}

.top-row {
    background: var(--silver2-color);
    border-radius: 20px;
    display: flex;
    justify-content: space-between;
    width: 100%;
    cursor: copy;
}

.top-row span {
    display: flex;
    align-items: center;
    margin: 8px 20px;
    justify-content: flex-start;
    
    overflow: hidden;
    white-space: nowrap;
    text-overflow: ellipsis;
    
}

.top-row div {
    display: flex;
}

.top-row div button {
    border: none;
    background: #a7ceee;
    display: flex;
    padding: 8px;
    align-items: center;
    justify-content: center;
}

.top-row button img {
    width: 25px;
    height: 25px;
}

.top-row div button:hover {
    background: #b9ddfc;
}

.top-row span img {
    height: 20px;
    margin-right: 8px;
}

.bottom-row {
    padding: 8px 20px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

#ctx-message {
    background-color: #fff;
    border: 1px solid #000;
    position: absolute;
    display: none;
    font-size: 12px;
    padding: 4px;
}
</style>