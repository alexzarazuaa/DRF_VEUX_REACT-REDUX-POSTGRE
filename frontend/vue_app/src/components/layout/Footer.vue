<template>
<footer>
  <div class="container">
    <a class="logo"> © KALYPSO</a>
    <span class="attribution" style="background-color: black;">
    </span>
  </div>
</footer>
</template>

<script>
export default {
  name: "Footer"
};

</script>

<style>
footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    color: white;
    text-align: center;
    background-color: white;
}
.logo {
    color: black;
    text-align: center;
    padding: 12px;
    text-decoration: none;
    line-height: 10px;
    border-radius: 4px;
    font-size: 25px;
    font-weight: bold;
}
</style>
