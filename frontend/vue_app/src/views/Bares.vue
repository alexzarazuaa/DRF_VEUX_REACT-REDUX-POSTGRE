<template>
  <div class="banner">
    <div class="container">
      <h1 class="logo-font">SEEK BAR</h1>
      <p> BARES ONTINYENT</p>
    </div>
  </div>

  <section class="bares">
    <BarsList />
  </section>
</template>


<script>
  import BarsList from '@/components/BarsListComponent/BarsList'
  export default {
    name: "Bares",
    components: {
      BarsList,
    },
  }
  
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
.logo,.font{

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
.bares {
  padding: 10px;
   margin-top: 100px;
  margin-bottom: 100px;
}


</style>