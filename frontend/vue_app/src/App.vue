<template>
  <section class = "wrapper">
    <NavbarComponent />
    <HeaderComponent />
    <div class = "content">
    </div>
    <RouterView />
  </section>
</template>

<script>
import HeaderComponent from "./components/layout/HeaderComponent.vue";
import { defineComponent } from 'vue'
export default defineComponent({
  name: "App",
  components: {
    HeaderComponent,
  },
})
</script>

<style>
body {
  margin: 0;
  padding: 0;
  background: #1f1f1f;
}
.wrapper {
  display: grid;
  grid-template-areas: 
    "navbar header"
    "navbar content";
  grid-template-columns: 300px auto;
  grid-template-rows: 100px auto;
}
.content {
  grid-area: "content";
}
</style>