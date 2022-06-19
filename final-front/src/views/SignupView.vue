<template>
  <div class="container">
    <h1>Signup</h1>
    <div class="d-flex align-items-center flex-column">
      <account-error-list v-if="authError"></account-error-list>
      <form @submit.prevent="signup(credentials)" style="width:300px;">
        <div class="my-2 d-flex flex-column align-items-start">
        <label for="username">Username </label>
        <b-form-input v-model="credentials.username" type="text" id="username" placeholder="username" required></b-form-input>
        </div>
        <div class="d-flex flex-column align-items-start mb-2">
          <label for="password1">Password </label>
          <b-form-input v-model="credentials.password1" type="password" id="password1" placeholder="password1" required></b-form-input>
        </div>
        <div class="d-flex flex-column align-items-start mb-2">
          <label for="password2">Password Confirmation </label>
          <b-form-input  v-model="credentials.password2" type="password" id="password2" placeholder="password2" required></b-form-input>
        </div>
        <div>
          <button class="btn btn-warning">Sign Up</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  import AccountErrorList from '@/components/AccountErrorList.vue'

  export default {
    name: 'SignupView',
    components: {
      AccountErrorList,
    },
    data() {
      return {
        credentials: {
          username: '',
          password1: '',
          password2: '',
        }
      }
    },
    computed: {
      ...mapGetters(['authError'])
    },
    methods: {
      ...mapActions(['signup'])
    },
  }
</script>

<style></style>
