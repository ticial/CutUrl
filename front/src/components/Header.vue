<script>

export default {
    props: ['logout'],
    data() {
        return {
            nav_button: document.querySelector('#nav-toggle'),
            nav_bar: document.querySelector('.nav'),
            nav_bar_visible: true,
            nav_button_visible: false
        }
    },
    methods: {
        onResize() {
            if (window.innerWidth > 700) {
                this.nav_bar_visible = true
                this.nav_button_visible = false
            } else {
                this.nav_bar_visible = false
                this.nav_button_visible = true
            }
        }
    },
    created: function () {
        window.addEventListener('resize', this.onResize)
    },
    destroyed: function () {
        window.removeEventListener('resize', this.onResize)
    },
    mounted() {
        this.onResize()
    }
}
</script>

<template>
    <header class="container">
        <RouterLink to="/" active-class="active">
            <h1>Linker</h1>
        </RouterLink>
        <div>
            <img v-if="nav_button_visible" id="nav-toggle" @click="nav_bar_visible = !nav_bar_visible"
                src="/img/bars-solid.svg" alt="Навигация" title="Навигация">
            <ul v-if="nav_bar_visible" class="nav">
                <li v-if="$store.state.isAuthenticated">
                    <RouterLink to="/links" active-class="active">Ссылки</RouterLink>
                </li>
                <li>
                    <RouterLink to="/" active-class="active">Про нас</RouterLink>
                </li>
                <li v-if="!$store.state.isAuthenticated">
                    <RouterLink to="/register" active-class="active">Регистрация
                    </RouterLink>
                </li>
                <li v-else>
                    <RouterLink to="/profile" active-class="active">Профиль</RouterLink>
                </li>
                <li v-if="!$store.state.isAuthenticated">
                    <RouterLink to="/login" active-class="active">Войти</RouterLink>
                </li>
                <li v-else><a @click="logout()" active-class="active">Выйти</a></li>
            </ul>
        </div>

    </header>
</template>

<style scoped>

@media (max-width: 700px) {
    header {
        padding: 16px 20px;
    }

    .nav {
        flex-direction: column;
        display: none;
        position: absolute;
        top: 60px;
        right: 0;
        background-color: var(--silver2-color);
        border: 2px solid var(--silver1-color);
        border-radius: 10px;
    }

    #nav-toggle {
        display: block;
    }
}

@media (min-width: 701px) {
    .nav {
        flex-direction: row;
        position: relative;
    }

    #nav-toggle {
        display: none;
    }
}

#nav-toggle {
    width: 32px;
    height: 32px;
}

header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding-top: 16px;
    padding-bottom: 16px;
    position: relative;
    background: var(--silver2-color);
    border-bottom: 2px solid var(--silver1-color);
}

.nav {
    list-style: none;
    display: flex;
}

.nav li {
    display: block;
    margin-left: 12px;
    cursor: pointer;
    padding: 8px 16px;
}

.nav li .active {
    text-decoration: underline;
    color: var(--hover-color);
}

.nav li a {
    position: relative;
}
</style>