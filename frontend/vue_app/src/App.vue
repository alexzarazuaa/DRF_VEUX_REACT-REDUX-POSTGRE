<template>
  <section>
    <HeaderComponent />
    <FooterComponent />
    <div class = "content">
    </div>
    <RouterView />
  </section>
</template>

<script>
import FooterComponent from "./components/layout/FooterComponent.vue";
import HeaderComponent from "./components/layout/HeaderComponent.vue"
import { defineComponent } from 'vue'
export default defineComponent({
  name: "App",
  components: {
    FooterComponent,
    HeaderComponent
  },
})
</script>

<style>

</style>