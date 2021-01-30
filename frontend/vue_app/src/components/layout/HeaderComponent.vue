<template>
  <section class="header">
    <h1 class = "header__icons">Reproduce</h1>
  </section>
</template>

<script>
export default {
  name: "HeaderComponent",
  components: {},
};
</script>

<style>
.header {
  padding: 5px;
  background: rgba(45, 45, 45, 0.88);
  grid-area: "header";
}
.header__icons {
  color: rgba(235, 235, 245, 0.6);
}
</style>