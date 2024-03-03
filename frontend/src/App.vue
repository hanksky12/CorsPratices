<template>
  <div id="app">
    <h1>{{ message }}</h1>
    <button @click="sendCORSRequest">Send CORS Request</button>
  </div>
</template>

<script>
// import axios from 'axios';
export default {
  data() {
    return {
      message: 'Loading...',
    };
  },
  methods: {
      async sendCORSRequest() {
      try {
        const response = await fetch('https://127.0.0.1:8888/cors/api/data', {
          method: 'DELETE',
          credentials: 'include',
        });
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        const data = await response.json();
        this.message = data.message;
      } catch (error) {
        console.error('Error sending PUT request:', error);
        this.message = 'Error sending PUT request';
      }
    },
  },
  async created() {
    try {
      const response = await fetch('http://localhost:80/original/api/data');
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      const data = await response.json();
      this.message = data.message;
    } catch (error) {
      console.error('Error fetching data:', error);
      this.message = 'Error fetching data';
    }
  },
};
</script>

<style>
#app {
  font-family: Arial, sans-serif;
  text-align: center;
}
</style>

