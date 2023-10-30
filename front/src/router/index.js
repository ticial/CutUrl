import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            name: 'home',
            component: () => import('../views/AboutView.vue')
        },
        {
            path: '/links',
            name: 'links',
            component: () => import('../views/LinksView.vue')
        },
        {
            path: '/register',
            name: 'register',
            component: () => import('../views/RegisterView.vue')
        },
        {
            path: '/login',
            name: 'login',
            component: () => import('../views/LoginView.vue')
        },
        {
            path: '/profile',
            name: 'profile',
            component: () => import('../views/ProfileView.vue')
        },
        {
            path: '/:pathMatch(.*)*',
            redirect: '/404'
        },
        {
            path: '/404',
            name: '404',
            component: () => import('../views/PageNotFound.vue')
        }

    ]
})

export default router
