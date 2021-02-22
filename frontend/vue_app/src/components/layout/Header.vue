<template>
  <section class="header">
    <nav class="header__nav">
      <section class="logo">
        <router-link to="/home">Home</router-link>
      </section>

      <div class="navbar">
        <router-link to="/bares">Bares</router-link>
        <router-link to="/contact">Contact</router-link>
        <router-link v-if="!isAuthenticated" to="/login">Login</router-link>
        <router-link v-if="!isAuthenticated" to="/register"
          >Register</router-link
        >
        <a @click="profile(currentUser.username)">
          {{ currentUser.username }}
        </a>

        <a class="Btn-logout" v-if="isAuthenticated" @click="logout">LogOut</a>
      </div>
    </nav>
  </section>
</template>

<script>
import { ActionsType } from "@/store/actions.type";
import { mapGetters } from "vuex";
export default {
  name: "Header",

  mounted() {
    this.VAL_TOKEN();
  },

  computed: {
    ...mapGetters(["currentUser", "isAuthenticated"]),
  },
  methods: {
    logout() {
      this.$store.dispatch(ActionsType.LOGOUT);
    },
    VAL_TOKEN() {
      this.$store.dispatch(ActionsType.CHECK_AUTH);
    },
    profile(username) {
      this.$router.push({ name: "Profile", params: { username: username } });
    },
  },
  //    watch: {
  //       currentUser: {
  //         deep: true,
  //         handler (value) {
  //           console.log('watch currentUser' , value)
  //         }
  //   }
  // }
};
</script>

<style>
* {
  box-sizing: border-box;
}
.header {
  overflow: hidden;
  background-color: #f1f1f1;
  padding: 10px 10px;
}

.logo {
  font-size: 25px;
  font-weight: bold;
}

.header a {
  margin-left: 20px;
}

.header a:hover {
  background-color: #ddd;
  color: black;
}

.header__nav {
  width: 100%;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  margin-bottom: 20px;
}

a,
a:visited,
a:active {
  color: black;
  text-decoration: none;
}

.navbar {
  float: left;
  color: black;
  text-align: center;
  padding: 12px;
  text-decoration: none;
  font-size: 18px;
  line-height: 25px;
  border-radius: 2px;
  font-weight: bold;
  cursor: pointer;
}

.navbar a:hover {
  background-color: #ddd;
  color: black;
}
.navbar a.active {
  background-color: dodgerblue;
  color: white;
}

.Btn-logout {
  cursor: pointer;
}
.Btn-logout a:hover {
  background-color: red;
  color: red;
}
</style>
