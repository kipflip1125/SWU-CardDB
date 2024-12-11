from rest_framework import serializers
from cards.models import SwCard, SwSet

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = SwCard
        fields = ('id', 'name', 'setid', 'aspects', 'traits', 'card_type', 'arena', 'artist', 'rarity', 'cost', 'power', 'health', 'keywords', 'frontimage', 'setcardid', 'unique', 'doublesided',
        'subtitle', 'backimage', 'epicaction', 'fronttext', 'backtext', 'variant')


class SetSerializer(serializers.ModelSerializer):
    class Meta:
        model = SwSet
        fields = ('id', 'name', 'setcode', 'releasedate')