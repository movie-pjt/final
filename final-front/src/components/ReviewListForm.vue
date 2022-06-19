<template>
  <div class="container d-flex mt-4 mb-5">
		<hr>
		<form action="" @submit.prevent="submitReview">
			<div class="mt-2">
				<label for="review-title" class="review-text mx-1">Title</label>
			</div>
				<div class="d-flex align-items-center">
				<input type="text" name="review-title" v-model="reviewTitle"
				class="review-input" placeholder="제목을 입력해주세요." required
				autofocus>
				<!-- <label for="review-vote" class="ms-4 me-3 review-text">Vote</label> -->
				<img src="@/assets/img/star.png" alt="" style="width: 25px;" class="ms-4 me-2">
				<input type="number" name="review-vote" v-model="reviewVote"
				class="vote-input" min="0" max="10">
				</div>
			<div class="my-2">
				<label for="review-content" class="review-text mx-1 mt-2">Content</label>
			</div>
			<div class="d-flex">
				<input type="text" name="review-content" v-model="reviewContent"
				class="review-input" placeholder="내용을 입력해주세요." required
				autofocus style="height: 100px">
				<div class="d-flex align-items-end">
					<button class="Submit-btn ms-4 me-2">Submit</button>
				</div>
			</div>
		</form>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'


export default {
	name: 'ReviewListForm',
  data() {
    return {
			reviewTitle: '',
      reviewContent: '',
			reviewVote: 10,
    }
	},
	computed: {
    ...mapGetters(['movie']),
  },
  methods: {
    ...mapActions(['createReview', 'fetchMovie']),
    submitReview() {
        const reviewBody = {
          title: this.reviewTitle,
          content: this.reviewContent,
          vote_average: this.reviewVote,
        }
				console.log(reviewBody)
        this.createReview({moviePk: this.$route.params.moviePk, review: reviewBody})
        this.fetchMovie(this.$route.params.moviePk)
        this.reviewTitle = ''
        this.reviewContent = ''
        this.reviewVote = 10
      },
  }

}
</script>

<style>

.review-text {
	font-family: 'Pretendard';
	font-size: 24px;
}

.review-input {
	border: 1px solid #fff;
	opacity: 0.8;
	background-color: #111111;
	border-radius: 7px;
	width: 500px;
	color: white;
	caret-color: white;
	padding:0;
	padding-left: 10px;
}

.vote-input {
	width: 60px;
	font-family: 'Pretendard';
	font-weight: 700;
	padding:0;
	padding-left: 5px;
	font-size: 20px;
	color: white;
	background-color: #111111;
	border: 1px solid #fff;
	opacity: 0.8;
	border-radius: 7px;
}

.Submit-btn {
	width: 90px;
	height: 50px;
	text-align: center;
	font-family: 'Pretendard';
	font-weight: 700;
	border-radius: 7px;
	transition: 0.5s;
}

.Submit-btn:hover {
	color: black;
	background: #E9BA13;
}
</style>