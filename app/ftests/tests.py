from django.test import LiveServerTestCase
from selenium import webdriver

from selenium.webdriver.common.keys import Keys

class PollsTest(LiveServerTestCase):
    
    options = {'username': 'admin', 'password': 'YourPasswordHere'}
    fixtures = ['admin_user.json']
        
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
        
    def tearDown(self):
        self.browser.quit()
        
    def test_can_create_new_poll_via_admin(self):
        self.browser.get(self.live_server_url + '/admin/')
        
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Django administration', body.text)

        username = self.browser.find_element_by_name('username')
        username.send_keys(self.options.get('username'))
        
        password = self.browser.find_element_by_name('password')
        password.send_keys(self.options.get('password'))
        
        password.send_keys(Keys.RETURN)
        
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Site administration', body.text)
        
        polls = self.browser.find_elements_by_link_text('Polls')
        self.assertEquals(len(polls), 2)
        
        polls[1].click()
        
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('0 polls', body.text)

        new_poll = self.browser.find_element_by_link_text('Add poll')
        new_poll.click()
        
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Question:', body.text)
        self.assertIn('Created at:', body.text)
        
        question = self.browser.find_element_by_name('question')
        question.send_keys("Challenge accepted?")

        date = self.browser.find_element_by_name('created_at_0')
        date.send_keys('02/21/13')
        
        time = self.browser.find_element_by_name('created_at_1')
        time.send_keys('00:00')

        choice_1 = self.browser.find_element_by_name('choice_set-0-choice')
        choice_1.send_keys('Yes')
        choice_2 = self.browser.find_element_by_name('choice_set-1-choice')
        choice_2.send_keys('Maybe')
        choice_3 = self.browser.find_element_by_name('choice_set-2-choice')
        choice_3.send_keys('No')
        
        save = self.browser.find_element_by_css_selector("input[value='Save']")
        save.click()
        
        new_poll = self.browser.find_elements_by_link_text("Challenge accepted?")
        self.assertEquals(len(new_poll), 1)
        