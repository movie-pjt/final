<template>
  <nav class="navbar navbar-expand-lg navbar-dark fixed-top" style="background-color:#111111;">
      <div class="container-fluid">
        <!-- <a class="navbar-brand" href="#">Uoir</a> -->
        <router-link to="/" class="navbar-brand"><img src="@/assets/img/logo2.png" alt="" width="100px;"></router-link>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
              <router-link to="/movies" class="nav-link">영화 목록</router-link>
            </li>
            <li class="nav-item">
              <router-link to="/articles" class="nav-link">커뮤니티</router-link>
            </li>
            <li class="nav-item">
              <router-link to="/discuss" class="nav-link">토론/논쟁</router-link>
            </li>
          </ul>
          <ul class="navbar-nav mb-2 mb-lg-0">
            <li class="nav-item" v-if="!isLoggedIn">
              <router-link to="/login" class="nav-link">Sign in</router-link>
            </li>
            <button class="btn btn-warning" type="submit" v-if="!isLoggedIn" @click="signUp">Sign Up</button>
            <li class="nav-item" v-if="isLoggedIn">
              <router-link to="/logout" class="nav-link">logout</router-link>
            </li>
            <li class="nav-item" v-if="isLoggedIn">
              <router-link :to="{ name: 'profile', params: { username } }" class="nav-link">{{ username }}</router-link>
            </li>
          </ul>
        </div>
      </div>
    </nav>
</template>

<script>
  import { mapGetters } from 'vuex'

  export default {
    name: 'NavBar',
    computed: {
      ...mapGetters(['isLoggedIn', 'currentUser']),
      username() {
        return this.currentUser.username ? this.currentUser.username : 'guest'
      },
    },
    methods: {
      signUp: function() {
        this.$router.push('signup')
      }
    }
  }
</script>

<style>
  nav .nav-link{
    font-family: 'Hahmlet';
    font-weight: 900;
    font-size:1.1rem;
  }

    nav .nav-link:hover{
    font-family: 'Hahmlet';
    font-weight: 900;
    font-size:1.1rem;
  }

  .navbar-brand {
    font-family: 'Hahmlet';
    font-weight: 900;
    font-size:1.1rem;
  }
</style>