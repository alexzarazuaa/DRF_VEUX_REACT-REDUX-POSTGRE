<template>
  <section>
    <div class="banner">
      <div class="container">
        <h1 class="logo-font">SEEK BAR</h1>
        <p>MAKE YOUR RESERVATION IN THE BEST BARS</p>
      </div>
    </div>
    <div class="list">
      <BarsList />
    </div>
  </section>
</template>

<script>
import BarsList from "@/components/BarsListComponent/BarsList";
export default {
  name: "Home",
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

.logo,
.logo-font {
  text-align: center;
  padding: 12px;
  text-decoration: none;
  font-size: 18px;
  line-height: 25px;
  border-radius: 4px;
  font-size: 25px;
  font-weight: bold;
}

.list {
  padding: 10px;
  width: 100vw;
  box-sizing: border-box;
  padding: 50px;
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr;
}
</style>
