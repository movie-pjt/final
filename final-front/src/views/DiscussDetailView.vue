<template>
  <div class="container my-5">
    <div class="d-flex flex-column align-items-start article-detail-div py-5 px-5 mb-5 overflow-auto">
      <div class="article-title py-3 d-flex justify-content-between mb-3">
        <h1>{{ discuss.title }}</h1>
      </div>
      <div class="vote-content my-3 d-flex flex-column mb-5 px-5">
        <div class="vote-div d-flex align-items-center">
          <div
          @click="choiceDiscuss('A')"
          class="discuss-detail-card vote-a me-4 d-flex justify-content-center align-items-center">
            <!-- <img src="@/assets/img/rose_red.png" alt=""> -->
            <div class="d-flex flex-column vote-content justify-content-center">
              <span>{{ getContentA(discuss.content) }}</span>
              <span>{{ choiceACount() }}</span>
            </div>
          </div>
          <div class="vs">vs</div>
          <div
          @click="choiceDiscuss('B')"
          class="discuss-detail-card vote-b ms-4 d-flex justify-content-center align-items-center">
            <!-- <img src="@/assets/img/rose_blue.png" alt=""> -->
            <div class="d-flex flex-column vote-content justify-content-center">
              <span>{{ getContentB(discuss.content) }}</span>
              <span>{{ choiceBCount() }}</span>
            </div>
          </div>
        </div>
      </div>
        <!-- <img :src="discuss.img" alt=""> -->

      <discuss-comment-list :comments="discuss.comments"></discuss-comment-list>
    </div>
  </div>
</template>

<script>
  import { mapGetters, mapActions } from 'vuex'
  import DiscussCommentList from '@/components/DiscussCommentList.vue'

  export default {
    name: 'DiscussDetail',
    components: { 
      DiscussCommentList
    },
    data() {
      return {
        discussPk: this.$route.params.discussPk,
      }
    },
    computed: {
      ...mapGetters(['isAuthor', 'discuss']),
    },
    methods: {
      ...mapActions([
        'fetchdiscuss',
        'discussChoice',
      ]),
      getContentA: function(text) {
				return text.split('vs')[0]
			},
      getContentB: function(text) {
				return text.split('vs')[1]
			},
      choiceACount: function() {
        return this.discuss.choice_a_users.length
      },
      choiceBCount: function() {
        return this.discuss.choice_b_users.length
      },
      isChoice: function() {
        return 1
      },
      choiceDiscuss: function(choice) {
        console.log(choice)
        this.discussChoice({discussPk: this.discuss.pk, choice: choice})
      }
    },
    created() {
      this.fetchdiscuss(this.discussPk)
    },
  }
</script>

<style>
.vote-content {
  font-family: "Pretendard";
  font-size: 1.3rem;
  height: 70%;
  width: 100%;
}
.vote-div {
  width: 100%;
  height: 400px;
  /* border: 2px solid white; */
}

.vote-a {
  width: 50%;
  background-color: #9c1e1e;
  transition: 1s;
  z-index: 0;
}

.vote-a:hover {
}

.vote-b {
  width: 50%;
  background-color: #40b3e5;
  transition: 1s;
  z-index: 0;
}

.vote-b:hover {
}

.discuss-detail-card:hover {
	/* left: 10px; */
  transform: translateY(-10px);
  box-shadow: rgba(255, 255, 255, 0.54) 0px 9px 20px;
}

.discuss-detail-card:hover::before {
	transform: scaleX(1);
}

.discuss-detail-card {
  position: relative;
  height: 18rem;
  color: white;
  /* background: #111111 !important; */
  border: 2px solid white !important;
  margin: 2rem;
  transition: 0.3s;
	cursor: pointer;
  border-radius: 10px;
}

.discuss-detail-card h5 {
  color:#E9BA13;
  transition: 1s;
  
}

.vote-content {
  font-size: 1.5rem;
}

.vs {
  font-family: 'hahmlet';
  font-weight: 800;
  font-size: 2rem;
}
</style>