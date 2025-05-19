<script setup>

import axios from 'axios';

import { ref } from 'vue';

const vectorData = ref("")

function sendData() {
    console.log("Sending request...")
    axios.post("http://localhost:5000/api/vector/store/text", {
        text: vectorData.value
    })
    .then(response => {
        console.log(response.data.response)
        vectorData.value = ""
    })
    .catch(function (error) {
        console.log(error);
    });
}

</script>

<template>
    <div>
        <div>
            <h3 class="title is-5">Data to be stored in the Vector DB</h3>
            <textarea v-model="vectorData" class="textarea" type="text" placeholder="Enter your data for RAG"></textarea>
            <input @click="sendData" class="button" type="submit" value="Send" />
        </div>
    </div>
</template>

<style scoped>
</style>