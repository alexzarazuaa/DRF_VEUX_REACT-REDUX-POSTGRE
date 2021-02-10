import Vue from "vue";
import Router from "vue-router";
import Home from '../views/Home.vue';
import Contact from '../views/Contact.vue';
import Bares from '../views/Bares.vue';
import Login from '../views/auth/Login.vue';
import Register from '../views/auth/Register.vue';

Vue.use(Router);

export default new Router({
  routes: [
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
      component: Login
    },
    {
      path: '/bares',
      name: 'Bares',
      component: Bares
    },
    {
      path: '/register',
      name: 'Register',
      component: Register
    },
    {
      path: "/:catchAll(.*)",
      redirect: '/',
    }
  ]

});
