import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import Home from '../views/Home.vue';
import Contact from '../views/Contact.vue';
import Bares from '../views/Bares.vue';
import Login from '../views/auth/Login.vue';
import Bar from '../views/Bar.vue';
import Profile from '../views/Profile.vue'
import Register from '../views/auth/Register.vue';

const noAuthGuard = (to: any, from: any, next: any) => {
  (localStorage.getItem("token")) ? next("/") : next()
}

const authGuard = (to: any, from: any, next: any) => {
  (!localStorage.getItem("token")) ? next("/login") : next()
}


const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/contact',
    name: 'Contact',
    component: Contact
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
    beforeEnter: noAuthGuard
  },
  {
    path: '/bares',
    name: 'Bares',
    component: Bares
  },
  {
    path: '/bar/:slug',
    name: 'Bar',
    props: true,
    component: Bar
  },
  {
    path: '/register',
    name: 'Register',
    component: Register,
    beforeEnter: noAuthGuard
  },
  {
    path: "/profiles/:username",
    name :"Profile",
    component: Profile,
    props: true,
    beforeEnter: authGuard
  },
  {
    path: "/:catchAll(.*)",
    redirect: '/',
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router