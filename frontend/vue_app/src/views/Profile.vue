<template>
      <h1>{{profile.username}}</h1>
</template>

<script>
import store from "@/store";
import { mapGetters } from "vuex";
import { ActionsType } from "@/store/actions.type";

export default {
  name: "Profile",
  mounted() {
    this.$store.dispatch(ActionsType.FETCH_PROFILE, this.$route.params);
  },
  beforeRouteEnter(to, from, next) {
    store.dispatch(ActionsType.FETCH_PROFILE, to.params.username);
    next();
  },
  computed: {
    ...mapGetters(["currentUser", "profile", "isAuthenticated"]),
  },
  methods: {
    isCurrentUser() {
      if (this.currentUser.username && this.profile.username) {
        return this.currentUser.username === this.profile.username;
      }
      return false;
    },
  },
  watch: {
    profile: {
      deep: true,
      handler(value) {
        console.log("watch currentUser", value);
      },
    },
  },
};
</script>
