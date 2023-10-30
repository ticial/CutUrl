<script>

const animation_time = 450

export default {
    name: 'MessageList',
    props: ['input_msgs', 'type', 'time'],
    data() {
        return {
            msgs: {},
            msg_id: 0,
        }
    },
    watch: {
        // отслеживаем изменение props input_msgs
        input_msgs() { 
            if (this.input_msgs) {
                this.msgs = {} // если есть новые сообщения - очищаем педыдущие мгновенно
                for (let el of this.input_msgs){
                    this.addMessage(el, this.type, this.time)
                }
            }else { // иначе с анимацией
                for(let id in this.msgs){
                    this.hideMessage(id)
                }
            }
        }
    },
    methods: {
        addMessage(text, type, time){
            const msg = {
                'text': text,
                'type': type,
                'state': 'start',
                'id': this.msg_id++,
            }
            this.msgs[msg.id] = msg

            if(time === 0) return

            setTimeout(() => {
                this.hideMessage(msg.id)
            }, time)
        },
        hideMessage(id) {
            this.msgs[id].state = 'end'
            setTimeout(() => {
                // этот блок кода нужен для избежания ошибки в v-for при удалении элемента объекта/массива
                const msgs = this.msgs
                delete msgs[id]
                this.msgs = {}
                this.msgs = msgs
            }, animation_time)
        }

    },
}
</script>

<template>
    <div class="centered-container-flex global-message-block">
        <div v-for="el in msgs" key="el.id">
            <li class="hint-block  mt-2" :class="{
                'success-block': el.type === 'success',
                'error-block': el.type === 'error',
                'animate__fadeIn': el.state === 'start',
                'animate__fadeOut': el.state === 'end',
            }">{{ el.text }}</li>
        </div>
    </div>
</template>

<style scoped>
@keyframes fadeInDown {
    from {
        opacity: 0;
    }

    to {
        opacity: 1;
    }
}

.animate__fadeIn {
    animation-duration: 500ms;
    -webkit-animation-name: fadeInDown;
    animation-name: fadeInDown;
    overflow: hidden;
}

@keyframes fadeOutUp {
    from {
        opacity: 1;
    }

    to {
        opacity: 0;
    }
}

.animate__fadeOut {
    animation-duration: 500ms;
    -webkit-animation-name: fadeOutUp;
    animation-name: fadeOutUp;
}
</style>