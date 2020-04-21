class Review:
    all_review = []
    def __init__(self, movie_id, title, imageurl, review):
        self.movie_id = movie_id
        self.title = title
        self.imageurl = imageurl
        self.review = review

    def save_review(self):
        Review.all_review.append(self)

    @classmethod
    def clear_reviews(cls):
        Review.all_review.clear()
        