<template>
  <div @click="details(bar.slug)" class="bar-preview">
    <p class="bar-title">{{ bar.name }}</p>
    <label class="bar-price">{{ bar.description }}</label>
  </div>
</template>


<script >
export default {
    name: "BarsPreview",
    component: {},
    props:[
         'bar'
    ]
   
  
  
}
</script>


<style>

.bar-preview {
  cursor: pointer;
  color: black;
  padding: 10px;
  margin: 10px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.bar-preview:hover {
  transition: 0.4s;
    background-color: #eeefff;
}
.bar-title {
  color: #ef5555;
}
.bar-title {
  transition: 0.4s;
  color: #3a3a3a;
  text-transform: capitalize;
  font-size: 1.2em;
  margin-bottom: 5px;
}
.bar-price {
  font-weight: bold;
}

</style>