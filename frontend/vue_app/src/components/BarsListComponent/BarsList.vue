<template>
  <div class="list">

    <div v-for="bar in bars" :key="bar">
      <BarsPreview  v-bind:bar="bar"/>
    </div>

  </div>
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
    ...mapGetters(['bars']),
  
  },

  watch: {
    bars: {
      deep: true,
      handler (value) {
        console.log('watch Bars' , value)
      }
    }
}


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
