<template>
  <div class="banner">
    <div class="container">
      <h1 class="logo-font">KALYPSO</h1>
      <p>A place to shop your <i>QUALITY</i> CLOTH.</p>
    </div>
  </div>
</template>



<script lang="ts">
  import { Vue } from 'vue-class-component';
  export default class Home extends Vue {}
</script>


<style>


.container{
  display: inline-block;
  color: white;
  text-align: center;
  padding: 52px;
  text-decoration: none;
}
.banner{
  background-color: black;
}

.banner_brands{
  color: black;
  display: flex;
  justify-content: center;
  align-items: center;
}
.logo {

  color: black;
  text-align: center;
  padding: 12px;
  text-decoration: none;
  font-size: 18px;
  line-height: 25px;
  border-radius: 4px;
  font-size: 25px;
  font-weight: bold;
}


</style>