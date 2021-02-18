<template>
  <section>
    <div class="list">
      <div v-for="bar in bars" :key="bar">
        <BarsPreview v-bind:bar="bar" />
      </div>
    </div>

    <!-- <article>
      <a href="#" class="previous round">&#8249;</a>
      <a href="#" class="next round">&#8250;</a>
    </article> -->
    
  </section>
</template>

<script>
import BarsPreview from "./BarsPreview";
import { mapGetters } from "vuex";
import { ActionsType } from "../../store/actions.type";
export default {
  name: "BarsList",
  components: {
    BarsPreview,
  },
  mounted() {
    this.$store.dispatch(ActionsType.FETCH_BARS);
  },
  computed: {
    ...mapGetters(["bars"]),
  },

  watch: {
    bars: {
      deep: true,
      handler(value) {
        console.log("watch Bars", value);
      },
    },
  },
};
</script>

<style>
.list {
  width: 100%;
  box-sizing: border-box;
  padding: 10px;
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr;
}


</style>
