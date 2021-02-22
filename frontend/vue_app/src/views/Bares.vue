<template>
  <section class="bares">
    <h1 class="title">BARES</h1>
    <BarsList />
  </section>
</template>

<script>
import BarsList from "@/components/BarsListComponent/BarsList";
export default {
  name: "Bares",
  components: {
    BarsList,
  },
};
</script>

<style>
.container {
  display: inline-block;
  color: white;
  text-align: center;
  padding: 52px;
  text-decoration: none;
}
.banner {
  background-color: black;
}

.title {
  color: black;
  text-align: center;
  padding: 12px;
  text-decoration: none;
  font-size: 18px;
  line-height: 25px;
  border-radius: 4px;
  font-size: 45px;
  font-weight: bold;
}
.bares {
  padding: 10px;
  margin-top: 100px;
  margin-bottom: 100px;
}
</style>
