<template>
  <div>
    <h1>Login</h1>
    <div class="d-flex align-items-center flex-column">
      <account-error-list v-if="authError"></account-error-list>
      <form @submit.prevent="login(credentials)" style="width:300px;">
        <div class="d-flex flex-column align-items-start my-2">
          <label for="username" class="input-label mx-2">username </label>
          <!-- <input v-model="credentials.username" type="text" id="username" required /> -->
          <b-form-input id="username" v-model="credentials.username" type="text" placeholder="Username" required></b-form-input>
        </div>
        <div class="d-flex flex-column align-items-start mb-2">
          <label for="password" class="input-label mx-2">password </label>
          <!-- <input v-model="credentials.password" type="password" id="password" required /> -->
          <b-form-input id="password" v-model="credentials.password" type="password" placeholder="Password" required></b-form-input>
        </div>

        <button class="btn btn-warning">Login</button>
      </form>
    </div>
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  import AccountErrorList from '@/components/AccountErrorList.vue'

  export default {
    name: 'LoginView',
    components: {
      AccountErrorList,
    },
    data() {
      return {
        credentials: {
          username: '',
          password: '',
        }
      }
    },
  computed: {
      ...mapGetters(['authError'])
    },
    methods: {
      ...mapActions(['login'])
    },
  }
</script>

<style>
.input-label {
  font-size: 1.2rem;
}
</style>
