<script setup></script>

<template>
    <footer class="container footer mt-5">
        <p>Все права защищены ©</p>
        <div class="social-links">
            <img src="/img/vk.svg">
            <img src="/img/youtube.svg">
            <img src="/img/square-twitter.svg">
        </div>
    </footer>
</template>

<style scoped>
@media (max-width: 700px) {
    footer {
        padding: 16px 20px;
        flex-direction: column;
    }

    .social-links {
        margin-top: 16px;
    }
}

.social-links {
    display: flex;
    gap: 32px;
}

.social-links img {
    height: 32px;
}

.footer {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding-top: 16px;
    padding-bottom: 16px;
    background: var(--silver2-color);
    border-top: 2px solid var(--silver1-color);
}
</style>