{"filter":false,"title":"test_forms.py","tooltip":"/todo/test_forms.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":13,"column":75},"action":"insert","lines":["from django.test import TestCase","from .forms import ItemForm","","# Create your tests here.","class TestToDoItemForm(TestCase):","","    def test_can_create_an_item_with_just_a_name(self):","        form = ItemForm({'name': 'Create Tests'})","        self.assertTrue(form.is_valid())","    ","    def test_correct_message_for_missing_name(self):","        form = ItemForm({'form': ''})","        self.assertFalse(form.is_valid())","        self.assertEqual(form.errors['name'], [u'This field is required.'])"],"id":1}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":13,"column":75},"end":{"row":13,"column":75},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1584532666834,"hash":"4880331ccad7e7d3df44e93e5f1781d802ea254a"}