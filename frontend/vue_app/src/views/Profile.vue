<template>
  <section>
    <article class="userInfo">
      <img class="ImgProfile" v-bind:src="profile.image" />
      <h1 class="userInfo_Name">{{ profile.username }}</h1>
    </article>

    <!-- <h2 class="titleFavoriteds">YOUR FAVORITEDS</h2> -->
    <!-- <BarsList :favorited="favorited" /> -->
  </section>
</template>

<script>
import store from "@/store";
import { mapGetters } from "vuex";
//import BarsList from '@/components/BarsListComponent/BarsList'
import { ActionsType } from "@/store/actions.type";

export default {
  name: "Profile",
  // components:{BarsList},
  mounted() {
    this.$store.dispatch(ActionsType.FETCH_PROFILE, this.$route.params);
  },
  beforeRouteEnter(to, from, next) {
    store.dispatch(ActionsType.FETCH_PROFILE, to.params.username);
    next();
  },
  computed: {
    ...mapGetters(["profile"]),
  },
  watch: {
    profile: {
      deep: true,
      handler(value) {
        console.log("watch profile", value);
      },
    },
  },
};
</script>

<style scoped>
.userInfo {
  padding-top: 74.3px;
  padding-bottom: 71px;
  border-bottom: lightcoral 2px solid;
  text-align: center;
  background-color: palegoldenrod;
}
.userInfo_Name {
  color: black;
  text-align: center;
  padding: 12px;
  text-decoration: peru;
  line-height: 10px;
  border-radius: 4px;
  font-size: 25px;
  font-weight: bold;
}

.ImgProfile {
  margin-top: 15px;
  border-radius: 30px;
}
.titleFavoriteds:hover {
  text-decoration: underline grey;
}
</style>
