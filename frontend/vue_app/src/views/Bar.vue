<template>
  <div class="bar-details">
    <div class="bar-main">

      <div class="bar-info">
        <h1 class="bar-title">{{ bar.name }}</h1>
      </div>
    </div>
  
    <div class="bar-description">
        <h3>Description</h3>
        <p>{{ bar.description }}</p>
    </div>
       <div class="bar-owner">
        <h3>Owner</h3>
        <p>{{ bar.owner.username }}</p>
    </div>
  </div>
</template>



<script>

import store from "@/store";
import { mapGetters } from "vuex";
import { ActionsType } from "@/store/actions.type";
export default {
  name: 'Bar',
  props: {
    slug: {
      type: String,
      required: true
    }
  },
  beforeRouteEnter(to, from, next) {
    Promise.all([
      store.dispatch(ActionsType.FETCH_BAR, to.params.slug)
    ]).then(() => {
      next();
      console.log(to.params.slug)
    });
  },
  computed: {
      ...mapGetters(['bar']),
  },
    watch: {
    bar: {
      deep: true,
      handler (value) {
        console.log('watch a bar' , value)
      }
    }
    }
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
  margin-top: 80px;
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
.bar-title {
  text-transform: capitalize;
  color: black;
  display:flex;
  justify-content:center;
  align-items:center;
  align-content:center;
  font-size:32px;
  font-width:bold;
  font-family: "Lucida Console", "Courier New", monospace;
}
.bar-price {
  font-weight: bold;
  font-size: 1.2em;
}

.bar-description h3  , .bar-owner h3{
  margin-top: 10px;
  justify-content:center;
  align-items:center;
  align-content:center;
  font-size:22px;
  font-width:bold;
}

.bar-description, .bar-owner {
  width: 65%;
  margin-top: 30px;
  margin-bottom: 50px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.bar-description p  , .bar-owner p{
  margin-top: 10px;
}
</style>
