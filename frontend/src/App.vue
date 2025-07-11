<template>
  <div id="app">
    <header>
      <h1>Bienvenido a MiCasaYa - Estimación de Precios de Viviendas</h1>
    </header>
    <main>
      <PropertyEstimator />
    </main>
  </div>
</template>

<script>
import PropertyEstimator from './components/PropertyEstimator.vue';

export default {
  name: 'App',
  components: {
    PropertyEstimator
  }
};
</script>

<style scoped>
#app {
  font-family: 'Arial', sans-serif;
  text-align: center;
}
header {
  background-color: #282c34;
  padding: 20px;
  color: white;
}
</style>
