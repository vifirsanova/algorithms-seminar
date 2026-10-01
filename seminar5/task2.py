import heapq


class Twitter:
    """Упрощённая версия Twitter.

    Пользователи публикуют твиты, подписываются друг на друга
    и видят 10 самых свежих твитов в своей ленте.
    """

    def __init__(self):
        """Инициализировать пустой Twitter.

        Структуры данных:
            tweets: словарь userId -> список (timestamp, tweetId),
                отсортированный по возрастанию timestamp.
            following: словарь userId -> множество ID, на кого подписан.
            time: глобальный счётчик для timestamp, увеличивается
                при каждом postTweet.
        """
        self.tweets = {}
        self.following = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        """Опубликовать твит от пользователя userId.

        Args:
            userId: ID автора.
            tweetId: ID твита. Гарантируется уникальность каждого вызова.

        Returns:
            None.
        """
        self.time += 1
        self.tweets.setdefault(userId, []).append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> list[int]:
        """Вернуть 10 самых свежих твитов в ленте пользователя.

        Лента состоит из твитов самого пользователя и всех, на кого он
        подписан. Твиты упорядочены от самых свежих к самым старым.

        Args:
            userId: ID пользователя, чью ленту нужно построить.

        Returns:
            Список tweetId длиной не более 10, отсортированный
            от самых свежих к самым старым.
        """
        pass

    def follow(self, followerId: int, followeeId: int) -> None:
        """Пользователь followerId подписывается на followeeId.

        Args:
            followerId: ID подписчика.
            followeeId: ID того, на кого подписываются.

        Returns:
            None.
        """
        pass

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """Пользователь followerId отписывается от followeeId.

        Args:
            followerId: ID подписчика.
            followeeId: ID того, от кого отписываются.

        Returns:
            None.
        """
        pass
