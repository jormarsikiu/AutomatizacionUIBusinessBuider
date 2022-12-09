import allure

def allure_screenshot_fail(ImageFile, Feature):
    allure.attach.file(ImageFile, name="Click to download a Screenshot Error", attachment_type=allure.attachment_type.PNG)
    allure.attach.file(Feature, name="Click to download a Feature", attachment_type=allure.attachment_type.TEXT)
    
def allure_screenshot_only_fail(ImageFile):
    allure.attach.file(ImageFile, name="Click to download a Screenshot Error", attachment_type=allure.attachment_type.PNG)    

def allure_screenshot_success(Feature):
    allure.attach.file(Feature, name="Click to download a Feature", attachment_type=allure.attachment_type.TEXT)