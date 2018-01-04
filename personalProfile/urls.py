from django.conf.urls import url
from .views import personalProfileDetail, personalProfileSetting, personalProfileSettingMF
from .views import personalProfileDynamic
from .views import personalProfileFavourite
from .views import personalProfileBasicSetting
from .views import personalProfileDetailSetting
from .views import personalProfileBackList
from .views import personalProfileReward
from .views import personalProfileRedirectFollow
from .views import personalProfileRedirectBlackList
from .views import personalProfileBasic
from .views import personalProfileShowFollower
from .views import personalProfileShowFollowed

urlpatterns = [
    url(r'^mainPage/$', personalProfileDetail.as_view(), name='personalProfileMain'),
    url(r'^settingPage/$', personalProfileSettingMF, name='personalProfileSetting'),
    url(r'^basicSettingPage/$', personalProfileBasicSetting, name='personalProfileBasicSetting'),
    url(r'^basicPage/$', personalProfileBasic, name='personalProfileBasic'),
    url(r'^detailSettingPage/$', personalProfileDetailSetting, name='personalProfileDetailSetting'),
    url(r'^backListSettingPage/$',personalProfileBackList, name='personalProfileBackList'),
    url(r'^rewardSettingPage/$', personalProfileReward, name='personalProfileReward'),
    url(r'^dynamicPage/$', personalProfileDynamic, name='personalProfileDynamic'),
    url(r'^favouritePage/$', personalProfileFavourite, name='personalProfileFavourite'),
    url(r'^redirectFollow/$', personalProfileRedirectFollow, name='psersonalProfileRedirectFollow'),
    url(r'^redirectBlackList/$', personalProfileRedirectBlackList, name='personalProfileRedirectBlackList'),
    url(r'^showFollower/$', personalProfileShowFollower, name='personalProfileShowFollower'),
    url(r'^showFollowed/$', personalProfileShowFollowed, name='personalProfileShowFollowed'),
]
