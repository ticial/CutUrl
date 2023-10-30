<script setup></script>

<template>
  <div class="centered-container-flex">
    <h1 class="center">Короче - красивее!</h1>
    <p class="mt-4">Этот сайт создан для того, чтобы Ваши ссылки выглядели лучше. А также Вы сможете узнать, сколько было переходов по этим ссылкам!</p>
    <p class="center mt-4">Хотите попробовать?</p>
    <div class="center-items mt-4">
        <div v-if="!$store.state.isAuthenticated" class="button-group">
            <button type="button" @click="$router.push('/login')">Войти</button>
            <button type="button" @click="$router.push('/register')">Регистрация</button>
        </div>
        <button v-else type="button" @click="$router.push('/links')">Ссылки</button>
    </div>
  </div>
</template>

<style scoped>
p {
    text-indent: 20px;
    line-height: 200%;
}

.center-items {
    display: flex;
    justify-content: center;
}

button a {
    color: var(--light-color);
}
</style>
