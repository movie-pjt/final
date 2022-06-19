<template>
	<div class="container">
		<div class="review-list-item my-3">
    <!-- <router-link :to="{ name: 'profile', params: { username: review.user.username } }">
      {{ review.user.username }}
    </router-link> -->
		<div class="d-flex align-items-center">
			<div class="review-username">{{ review.user.username }}</div>
			<div>
				<div class="ms-3" v-if="!isEditing">
					<img 
					v-for="i in star"
					:key="`s_review#${review.id}` + i"
					src="@/assets/img/star.png" alt="" style="width: 15px; height: 15px;" class="">
					<img 
					v-for="i in semiStar"
					:key="`sS_review#${review.id}` + i"
					src="@/assets/img/semistar.png" alt="" style="width: 7.5px; height: 15px;">
				</div>
				<div v-if="isEditing">
					<img class="ms-3"
					src="@/assets/img/star.png" alt="" style="width: 15px; height: 15px;">
					<input type="number" v-model="payload.vote_average" class="me-3 edit-vote-input" min="0" max="10">
				</div>
			</div>
			</div>
		<div class="d-flex justify-content-between">
			<div>
				<div class="d-flex">
					<div v-if="!isEditing">
						<div class="review-title mt-1">{{ review.title }}</div>
					</div>
					<div v-if="isEditing">
						<input type="text" v-model="payload.title" class="me-3 mb-1 edit-input">
					</div>
				</div>
					<div class="d-flex flex-column">
						<div class="review-content mt-1"
						v-if="!isEditing">{{ review.content }}</div>
						</div>
						<div v-if="isEditing">
							<input type="text" v-model="payload.content" class="me-3 edit-input">
							<button @click="onUpdate" class="me-2 edit-btn">수정</button>
							<button @click="switchIsEditing" class="cancel-btn">취소</button>
						</div>
			</div>

			<span v-if="currentUser.username === review.user.username && !isEditing">
				<font-awesome-icon icon="fa-solid fa-pen-to-square" 
				@click="switchIsEditing"
				class="fa-2x ed-btn"/>
				<font-awesome-icon icon="fa-solid fa-trash-can" 
				@click="deleteReviewClick(review)"
				class="fa-2x ed-btn"/>
			</span>
		</div>
	</div>
	</div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'ReviewListItem',
  props: { review: Object },
  data() {
    return {
      isEditing: false,
      payload: {
        moviePk: this.review.movie,
        reviewPk: this.review.id,
        content: this.review.content,
				title: this.review.title,
				vote_average: this.review.vote_average
      },
			
    }
  },
  computed: {
    ...mapGetters(['currentUser', 'movie', 'profile']),
		star: function() {
			return parseInt(this.review.vote_average / 2)
		},
		semiStar: function() {
			return this.review.vote_average % 2
		},
  },
  methods: {
    ...mapActions(['updateReview', 'deleteReview', 'fetchMovie', 'fetchProfile']),
    switchIsEditing() {
      this.isEditing = !this.isEditing
    },
    onUpdate() {
      const newReview = {
        reviewPk: this.review.id,
        title: this.payload.title,
        content: this.payload.content,
        vote_average: this.payload.vote_average,
      }
			// console.log(newReview)
      this.updateReview(newReview)
			setTimeout(() => console.log('update!'), 100);
      this.fetchProfile(this.currentUser)
      this.fetchMovie(this.review.movie)
      this.isEditing = false
    },
    deleteReviewClick() {
			console.log('delete Click!')
      this.deleteReview(this.review.id),
			setTimeout(() => {
				this.fetchProfile(this.currentUser)
				this.fetchMovie(this.review.movie)
				}, 100);
    }
  }
}
</script>

<style>

.review-list-item {
	border: 1px solid white;
	border-radius: 7px;
	padding: 10px 20px 10px 20px;
	letter-spacing: 1px;
}

.review-username {
	font-family: 'Pretendard';
	font-weight: 500;
	font-size: 25px;
	color: #E9BA13;

}

.review-title {
	font-family: 'Pretendard';
	font-weight: 800;
}

.review-content {
	font-family: 'Pretendard';
	font-weight: 200;
}

.edit-vote-input {
	width: 60px;
	font-family: 'Pretendard';
	font-weight: 700;
	margin-left: 10px;
	padding:0;
	padding-left: 5px;
	font-size: 20px;
	color: white;
	background-color: #111111;
	border: 1px solid #fff;
	opacity: 0.8;
	border-radius: 7px;
}

.ed-btn {
	cursor: pointer;
	padding: 0px 0px 0px 20px;
	opacity: 0.5;
}

.ed-btn:hover {
	color: white;
	opacity: 1;
}


.edit {
	margin-right: 2px;
}

.edit-input {
	width: 400px;
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

.edit-btn, .cancel-btn {
	width: 50px;
	height: 35px;
	text-align: center;
	font-family: 'Pretendard';
	font-weight: 700;
	border-radius: 7px;
	transition: 0.5s;
}

</style>