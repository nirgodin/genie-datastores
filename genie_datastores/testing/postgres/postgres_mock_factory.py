from collections import Counter
from random import randint, uniform

from genie_common.utils import (
    random_alphanumeric_string,
    random_enum_value,
    random_boolean,
    random_datetime,
    random_string_array
)

from genie_datastores.postgres.models import *
from genie_datastores.models import DataSource, EntityType
from genie_datastores.postgres.models.orm.spotify.spotify_featured_artist import SpotifyFeaturedArtist


class PostgresMockFactory:
    @staticmethod
    def case(**kwargs) -> Case:
        return Case(
            id=kwargs.get("id", random_alphanumeric_string()),
            endpoint=kwargs.get("endpoint", random_enum_value(PlaylistEndpoint)),
            playlist_id=kwargs.get("playlist_id", random_alphanumeric_string())
        )

    @staticmethod
    def case_progress(**kwargs) -> CaseProgress:
        return CaseProgress(
            id=kwargs.get("id"),
            case_id=kwargs.get("case_id", random_alphanumeric_string()),
            has_exception=kwargs.get("has_exception", random_boolean()),
            status=kwargs.get("status", random_alphanumeric_string()),
            time_took=kwargs.get("time_took", uniform(0, 30)),
            exception_details=kwargs.get("exception_details", random_alphanumeric_string())
        )

    @staticmethod
    def audio_features(**kwargs) -> AudioFeatures:
        return AudioFeatures(
            id=PostgresMockFactory._random_spotify_id(**kwargs),
            acousticness=PostgresMockFactory._random_confidence("acousticness", **kwargs),
            danceability=PostgresMockFactory._random_confidence("danceability", **kwargs),
            duration_ms=kwargs.get("duration_ms", randint(90000, 360000)),
            energy=PostgresMockFactory._random_confidence("energy", **kwargs),
            instrumentalness=PostgresMockFactory._random_confidence("instrumentalness", **kwargs),
            key=kwargs.get("key", randint(0, 11)),
            liveness=PostgresMockFactory._random_confidence("liveness", **kwargs),
            loudness=kwargs.get("loudness", randint(-60, 3)),
            mode=kwargs.get("mode", random_boolean()),
            speechiness=PostgresMockFactory._random_confidence("speechiness", **kwargs),
            tempo=PostgresMockFactory._random_confidence("tempo", **kwargs),
            time_signature=kwargs.get("time_signature", randint(0, 5)),
            valence=PostgresMockFactory._random_confidence("valence", **kwargs)
        )

    @staticmethod
    def spotify_track(**kwargs) -> SpotifyTrack:
        return SpotifyTrack(
            id=PostgresMockFactory._random_spotify_id(**kwargs),
            album_id=kwargs.get("album_id", random_alphanumeric_string()),
            artist_id=kwargs.get("artist_id", random_alphanumeric_string()),
            explicit=kwargs.get("explicit", random_boolean()),
            name=kwargs.get("name", random_alphanumeric_string()),
            number=kwargs.get("number", randint(1, 20)),
            release_date=kwargs.get("release_date", random_datetime()),
        )

    @staticmethod
    def spotify_artist(**kwargs) -> SpotifyArtist:
        return SpotifyArtist(
            id=PostgresMockFactory._random_spotify_id(**kwargs),
            name=kwargs.get("name", random_alphanumeric_string()),
            facebook_name=kwargs.get("facebook_name", random_alphanumeric_string()),
            genres=kwargs.get("genres", random_string_array()),
            instagram_name=kwargs.get("instagram_name", random_alphanumeric_string()),
            twitter_name=kwargs.get("twitter_name", random_alphanumeric_string()),
            wikipedia_language=kwargs.get("wikipedia_language", random_alphanumeric_string(min_length=2, max_length=2)),
            wikipedia_name=kwargs.get("wikipedia_name", random_alphanumeric_string()),
        )

    @staticmethod
    def track_lyrics(**kwargs) -> TrackLyrics:
        lyrics = kwargs.get("lyrics", random_string_array())
        joined_lyrics = " ".join(lyrics)
        tokens = joined_lyrics.split(" ")

        return TrackLyrics(
            id=PostgresMockFactory._random_spotify_id(**kwargs),
            lyrics=lyrics,
            lyrics_source=kwargs.get("lyrics_source", random_enum_value(DataSource)),
            language=kwargs.get("language", random_alphanumeric_string(min_length=2, max_length=2)),
            language_confidence=PostgresMockFactory._random_confidence("language_confidence", **kwargs),
            number_of_words=kwargs.get("number_of_words", randint(0, 600)),
            words_count=dict(Counter(tokens))
        )

    @staticmethod
    def artist(**kwargs) -> Artist:
        return Artist(
            id=PostgresMockFactory._random_spotify_id(**kwargs),
            shazam_id=PostgresMockFactory._random_shazam_id(key="shazam_id", **kwargs),
            birth_date=kwargs.get("birth_date", random_datetime()),
            death_date=kwargs.get("death_date", random_datetime()),
            birth_date_source=kwargs.get("birth_date_source", random_enum_value(DataSource)),
            gender=kwargs.get("gender", random_enum_value(Gender)),
            gender_source=kwargs.get("gender_source", random_enum_value(DataSource)),
            is_israeli=kwargs.get("is_israeli", random_boolean()),
            is_lgbtq=kwargs.get("is_lgbtq", random_boolean()),
            origin=kwargs.get("origin", random_alphanumeric_string()),
            country=kwargs.get("country", random_alphanumeric_string()),
            state=kwargs.get("state", random_alphanumeric_string()),
            county=kwargs.get("county", random_alphanumeric_string()),
            city=kwargs.get("city", random_alphanumeric_string()),
            latitude=kwargs.get("latitude", uniform(-90, 90)),
            longitude=kwargs.get("longitude", uniform(-180, 180)),
        )

    @staticmethod
    def radio_track(**kwargs) -> RadioTrack:
        return RadioTrack(
            id=kwargs.get("id"),
            track_id=PostgresMockFactory._random_spotify_id("track_id", **kwargs),
            added_at=kwargs.get("added_at", random_datetime()),
            artist_followers=kwargs.get("artist_followers", randint(0, 100000000)),
            artist_popularity=PostgresMockFactory._random_confidence("artist_popularity", **kwargs),
            popularity=PostgresMockFactory._random_confidence("popularity", **kwargs),
            snapshot_id=kwargs.get("snapshot_id", random_alphanumeric_string(min_length=64, max_length=64)),
            station=kwargs.get("station", random_enum_value(SpotifyStation))
        )

    @staticmethod
    def shazam_artist(**kwargs) -> ShazamArtist:
        return ShazamArtist(
            id=PostgresMockFactory._random_shazam_id(key="id", **kwargs),
            name=kwargs.get("name", random_alphanumeric_string()),
            birth_date=kwargs.get("birth_date", random_datetime()),
            genres=kwargs.get("genres", random_string_array()),
            origin=kwargs.get("origin", random_alphanumeric_string()),
            similar_artists=kwargs.get("similar_artists", random_string_array()),
        )

    @staticmethod
    def translation(**kwargs) -> Translation:
        return Translation(
            text=kwargs.get("text", random_alphanumeric_string()),
            translation=kwargs.get("translation", random_alphanumeric_string()),
            source_language=kwargs.get("source_language", random_alphanumeric_string()),
            target_language=kwargs.get("target_language", random_alphanumeric_string()),
            entity_id=kwargs.get("entity_id", random_alphanumeric_string()),
            entity_source=kwargs.get("entity_source", random_enum_value(DataSource)),
            entity_type=kwargs.get("entity_source", random_enum_value(EntityType))
        )

    @staticmethod
    def spotify_featured_artist(**kwargs) -> SpotifyFeaturedArtist:
        return SpotifyFeaturedArtist(
            id=kwargs.get("id"),
            track_id=PostgresMockFactory._random_spotify_id("track_id", **kwargs),
            artist_id=PostgresMockFactory._random_spotify_id("artist_id", **kwargs),
            position=kwargs.get("position", randint(1, 5)),
        )

    @staticmethod
    def chart_entry(**kwargs) -> SpotifyFeaturedArtist:
        return ChartEntry(
            id=kwargs.get("id"),
            chart=kwargs.get("chart", random_enum_value(Chart)),
            date=kwargs.get("date", random_datetime()),
            position=kwargs.get("position", randint(1, 100)),
            comment=kwargs.get("comment", random_alphanumeric_string()),
            entry_metadata=kwargs.get("entry_metadata"),
            key=kwargs.get("key", random_alphanumeric_string()),
            track_id=PostgresMockFactory._random_spotify_id("track_id", **kwargs),
        )

    @staticmethod
    def _random_confidence(key: str, **kwargs) -> int:
        return kwargs.get(key, randint(0, 100))

    @staticmethod
    def _random_spotify_id(key: str = "id", **kwargs) -> str:
        return kwargs.get(key, random_alphanumeric_string(min_length=22, max_length=22))

    @staticmethod
    def _random_shazam_id(key: str = "id", **kwargs) -> str:
        return kwargs.get(key, str(randint(10000, 2000000000)))
