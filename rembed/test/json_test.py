from rembed import parse

from hamcrest import *
from mock import *
import pytest

def test_should_parse_type_from_json():
    assert_that(get_response().type, equal_to('link'))

def test_should_parse_version_from_json():
    assert_that(get_response().version, equal_to('1.0'))

def test_should_parse_title_from_json():
    assert_that(get_response().title, equal_to('Lots of Bees'))

def test_should_parse_author_name_from_json():
    assert_that(get_response().author_name, equal_to('Ian Bees'))

def test_should_parse_author_url_from_json():
    assert_that(get_response().author_url, equal_to('http://www.example.com/ianbees/'))

def test_should_parse_provider_name_from_json():
    assert_that(get_response().provider_name, equal_to('Example'))

def test_should_parse_provider_url_from_json():
    assert_that(get_response().provider_url, equal_to('http://www.example.com/'))

def test_should_parse_cache_age_from_json():
    assert_that(get_response().cache_age, equal_to(3600))

def test_should_parse_thumbnail_url_from_json():
    assert_that(get_response().thumbnail_url, equal_to('http://www.example.com/bees/thumb.jpg'))

def test_should_parse_thumbnail_width_from_json():
    assert_that(get_response().thumbnail_width, equal_to(360))

def test_should_parse_thumbnail_height_from_json():
    assert_that(get_response().thumbnail_height, equal_to(240))

def test_should_parse_url_from_photo_json():
    assert_that(get_response('photo.json').url, equal_to('http://www.example.com/bees.jpg'))

def test_should_parse_width_from_photo_json():
    assert_that(get_response('photo.json').width, equal_to(600))

def test_should_parse_height_from_photo_json():
    assert_that(get_response('photo.json').height, equal_to(400))

def test_should_parse_html_from_video_json():
    assert_that(get_response('video.json').html, contains_string('http://www.example.com/bees.mpg'))

def test_should_parse_width_from_video_json():
    assert_that(get_response('video.json').width, equal_to(600))

def test_should_parse_height_from_video_json():
    assert_that(get_response('video.json').height, equal_to(400))

def test_should_parse_html_from_rich_json():
    assert_that(get_response('rich.json').html, contains_string('Bees!'))

def test_should_parse_width_from_rich_json():
    assert_that(get_response('rich.json').width, equal_to(600))

def test_should_parse_height_from_rich_json():
    assert_that(get_response('rich.json').height, equal_to(400))

def get_response(fixture = 'link.json'):
    return parse.parse_oembed_json(open('rembed/test/fixtures/json/' + fixture).read())