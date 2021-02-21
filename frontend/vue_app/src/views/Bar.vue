<template>
  <section class="bar-details">
    <article class="bar-main">
      <article class="bar-info">
        <h1 class="bar-title">{{ bar.name }}</h1>
      </article>
    </article>

    <article class="bar-description">
      <h3>Description</h3>
      <p>{{ bar.description }}</p>
    </article>

    <article class="bar-buttons">
      <button class="btn-primary" v-if="bar.favorited" @click="toggleFavorite">
        <i class="ion-heart"></i>&nbsp; &nbsp; &nbsp;
        <span class="counter"> {{ bar.favoritesCount }} </span>
      </button>

      <button class="btn-outline-primary" v-else @click="toggleFavorite">
        <i class="ion-heart"></i>&nbsp; &nbsp; &nbsp;
        <span class="counter"> {{ bar.favoritesCount }} </span>
      </button>
    </article>

    <article class="bar-buttons">
      <button @click="Reserva" style="font-size:24px">
        <span>RESERVAR</span>
      </button>
    </article>

    <article class="bar-owner">
      <h3>Owner</h3>
      <a class="ownerBar" @click="profile(currentUser.username)">
        {{ currentUser.username }}
      </a>
    </article>
  </section>
</template>

<script>
import store from "@/store";
import { mapGetters } from "vuex";
import { ActionsType } from "@/store/actions.type";
export default {
  name: "Bar",
  props: {
    slug: {
      type: String,
      required: true,
    },
  },
  beforeRouteEnter(to, from, next) {
    Promise.all([store.dispatch(ActionsType.FETCH_BAR, to.params.slug)]).then(
      () => {
        next();
      }
    );
  },

  computed: {
    ...mapGetters(["bar", "currentUser", "isAuthenticated"]),
  },
  methods: {
    toggleFavorite() {
      if (!this.isAuthenticated) {
        this.$router.push({ name: "Login" });
        return;
      }
      const action = this.bar.favorited
        ? ActionsType.FAVORITE_REMOVE
        : ActionsType.FAVORITE_ADD;
      this.$store.dispatch(action, this.bar.slug);
    },
    Reserva() {
      if (!this.isAuthenticated) {
        this.$router.push({ name: "Login" });
        return;
      }
    },
    profile(username) {
      this.$router.push({ name: "Profile", params: { username: username } });
    },
  },
  watch: {
    bar: {
      deep: true,
      handler(value) {
        console.log("watch a bar", value);
      },
    },
  },
};
</script>

<style>
.bar-details {
  padding: 10px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.bar-main {
  margin-top: 30px;
  width: 70%;
  display: flex;
  justify-content: space-around;
  align-items: flex-start;
  padding-bottom: 70px;
  border-bottom: 1px solid grey;
}
.bar-image {
  width: 40%;
}
.bar-info {
  color: #3a3a3a;
  width: 50%;
  text-align: center;
}
.ownerBar {
  color: black;
  text-align: center;
  padding: 12px;
  text-decoration: none;
  font-size: 18px;
  line-height: 25px;
  border-radius: 2px;
  font-weight: bold;

}

.ownerBar:hover {
  cursor: pointer;
  text-decoration: underline grey;
}
.buttons {
  width: 10%;
}
.btn-primary {
  background-color: coral;
  color: red;
}

.btn-outline-primary {
  background-color: green;
  color: whitesmokeΰ;
}
.counter,
.ion-heart {
  font-size: 25px;
  font-weight: bold;
}
.bar-title {
  text-transform: capitalize;
  color: black;
  display: flex;
  justify-content: center;
  align-items: center;
  align-content: center;
  font-size: 32px;
  font-weight: bold;
  font-family: "Lucida Console", "Courier New", monospace;
}
.bar-price {
  font-weight: bold;
  font-size: 1.2em;
}

.bar-description h3,
.bar-owner h3 {
  margin-top: 10px;
  justify-content: center;
  align-items: center;
  align-content: center;
  font-size: 22px;
  font-weight: bold;
}

.bar-description,
.bar-owner {
  width: 65%;
  margin-top: 10px;
  margin-bottom: 50px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.bar-description p,
.bar-owner p {
  margin-top: 10px;
}
</style>
