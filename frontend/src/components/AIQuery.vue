<script setup>

import axios from 'axios';

import { ref } from 'vue';

const question = ref("")
const answer = ref("")

function sendQuestion() {
    console.log(question.value)
    axios.post("http://localhost:5000/api/assistant/search", {
        query: question.value
    })
    .then(response => {
        console.log(response);
        answer.value = response.data.response.message.content;
    })
    .catch(function (error) {
        console.log(error);
    });
}

</script>

<template>
    <div>
        <div>
            <h3 class="title is-5">Ask the AI a question</h3>
            <input v-model="question" class="input is-rounded" type="text" placeholder="Enter your question"></input>
            <input @click="sendQuestion" class="button" type="submit" value="Send" />
        </div>
        <div>
            <h3 class="subtitle is-5">AI Response:</h3>
            <div class="box">{{ answer }}</div>
        </div>
    </div>
</template>

<style scoped>
</style>