<template>
	<div class="container">
		<div class="profile-article-list-item my-3">
		<div class="d-flex align-items-center">
			<div class="profile-article-username">{{ article.title }}</div>
			</div>
		<div class="d-flex justify-content-between">
			<div>
				<div class="d-flex">
						<div class="profile-article-title mt-1">{{ article.content }}</div>
				</div>
					<!-- <div class="d-flex flex-column">
						<div class="profile-article-content mt-1">
              {{ article.content }}</div>
          </div> -->
			</div>
		</div>
	</div>
	</div>
</template>

<script>

export default {
  name: 'ProfileArticleList',
  props: {
    article: Object
    },
  computed: {
  },
  methods: {
  }
}
</script>

<style>

.profile-article-list-item {
	border: 1px solid white;
	border-radius: 7px;
	padding: 10px 20px 10px 20px;
	letter-spacing: 1px;
}

.profile-article-username {
	font-family: 'Pretendard';
	font-weight: 500;
	font-size: 25px;
	color: #E9BA13;

}

.profile-article-title {
	font-family: 'Pretendard';
	font-weight: 800;
}

.profile-article-content {
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