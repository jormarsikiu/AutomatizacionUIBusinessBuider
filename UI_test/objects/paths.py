class Global():
    SelectOKDate = '''document.querySelectorAll(".dtp-btn-ok.btn.btn-success")[0].click();'''
    SelectOKDate2 = '''document.querySelectorAll(".dtp-btn-ok.btn.btn-success")[1].click();'''
    SelectOKDate3 = '''document.querySelectorAll(".dtp-btn-ok.btn.btn-success")[2].click();'''
    Accept = '''document.querySelector('.btn.btn-sm.btn-success').click()'''
    SaveAll = '''document.querySelector('.btn.btn-large.btn-outline-success.pull-right').click()'''
    Accept = '''document.querySelector('.btn.btn-sm.btn-success').click()'''
    AcceptModal = '''document.querySelector('.btn.btn-outline-success').click()'''
    #Menu
    ButtonBusiness = '''document.querySelectorAll("[href*='/dashboard/Business/index/MAP-003']")[0].click();'''
    ButtonSales = '''document.querySelectorAll("[href*='/dashboard/sales/SalesPanel/SAL-002']")[0].click();'''
    ButtonTransactions = '''window.location.href='https://test-xweb.eurokaizen.com/documents/transactions';'''
    #Search
    Search = '''document.querySelector('.col-11').click();'''
    FieldOpen = '''jQuery('#Field').select2('open')'''
    FieldCode = '''jQuery('#select2-Field-results li').first().trigger({type:'mouseup'})'''
    FieldOpenCondition = '''jQuery('[name="Condition"]').select2('open')'''
    FieldCondition = '''jQuery('.select2-results__options li').first().trigger({type:'mouseup'})'''
    AcceptSearch = '''document.querySelector('.btn.btn-sm.btn-success.btn-content-box.float-right').click();'''

class Login():
    ButtonCookie = '''document.querySelectorAll(".accept-policy.close")[0].click();'''
    ButtonLogin = '''document.querySelectorAll(".btn-block")[0].click();'''
    ButtonFlag = '''document.querySelector('#flag').click();'''
    ButtonSpanishFlag = '''document.querySelector('#es').click();'''
    ButtonEnglishFlag = '''document.querySelector('#en').click();'''
    ButtonAlemanFlag = '''document.querySelector('#de').click();'''
    ButtonSocietyAlcione = '''document.querySelectorAll("[href*='/Settings/User/ChangeCurrentSociety?societyCode=MS-01&url=~%2Fdashboard%2FBusiness%2Findex%2FMAP-003']")[0].click()'''
    ButtonSocietyMovilTruck = '''/Settings/User/ChangeCurrentSociety?societyCode=RYDER-01&url=~%2Fdashboard%2FBusiness%2Findex%2FMAP-003'''

class CreateUser():
    ButtonMenuUser = '''document.querySelectorAll("[href*='/settings/user']")[0].click()'''
    ButtonMenuUserNext = '''document.querySelectorAll('[href*="#next"]')[0].click();'''

class CreateBusinessPartner():
    ButtonBusinessPartner = '''window.location.href='/Management/BusinessPartner';'''
              #checar boton '''document.querySelectorAll("[href*='/Management/BusinessPartner']")[0].click();'''
    ButtonBusinessPartnerCreate = '''document.querySelectorAll("[href*='/Management/BusinessPartner/Form']")[0].click();'''
    SelectClientTypeOpen= '''jQuery('#EntityTypeCode').select2('open')'''
    SelectClientType= '''jQuery('#select2-EntityTypeCode-results li').first().trigger({type:'mouseup'})'''
    ButtonAddAddress = '''document.querySelectorAll("[href*='/Management/BusinessPartner/_AddressGeolocation']")[0].click();'''
    ButtonOpenTypeAddress = '''jQuery('#AddressEntityTypeCode').select2('open')'''
    ButtonTypeAddress = '''jQuery('#select2-AddressEntityTypeCode-results li').first().trigger({type:'mouseup'})'''
    ButtonIsDelivery = '''document.querySelectorAll("#IsDefaultDelivery")[0].click();'''
    #SelectAddress = '''jQuery('#pac-input').val($('.pac-container.pac-logo.hdpi').find('.pac-item').eq(0).text());'''
    clickAddress = '''document.querySelectorAll(".pac-container.pac-logo.hdpi div")[0].click()'''
    clickAddress2 = '''jQuery('.pac-container.pac-logo.hdpi').find('.pac-item').eq(1).trigger("click");'''
   # $('.pac-container.pac-logo.hdpi').show()  
    #Accounting
    ButtonAccounting = '''document.querySelectorAll("[href*='#tab1']")[0].click();'''
    ButtonAddAccounting = '''document.querySelectorAll("[href*='/Management/BusinessPartner/_Accountings']")[0].click();'''
    SelectOpenAccounting= '''jQuery('#selectParentAccounting').select2('open')'''
    SelectParentAccounting= '''jQuery('#select2-selectParentAccounting-results li').first().trigger({type:'mouseup'})'''
    SelectOpenChildAccounting = '''jQuery('#selectChildrenAccounting').select2('open')'''
    SelectChildAccounting= '''jQuery('#select2-selectChildrenAccounting-results li').first().trigger({type:'mouseup'})'''
    #Groups
    ButtonTapGroup = '''document.querySelectorAll("[href*='#tab2']")[0].click();'''
    ButtonAddBPGroup = '''document.querySelectorAll("[href*='/Management/BusinessPartner/_EntityGroups']")[0].click();'''
    #Business Condition
    ButtonBussCond = '''document.querySelectorAll("[href*='#tab3']")[0].click();'''
    SelectOpenBussCond = '''jQuery('#selectBusinessCondition').select2('open')'''
    SelectBussCond= '''jQuery('#select2-selectBusinessCondition-results li').first().trigger({type:'mouseup'})'''
    #Tax
    ButtonTax = '''document.querySelectorAll("[href*='#tab4']")[0].click();'''
    SelectOpenTax = '''jQuery('#selectTaxes').select2('open')'''
    SelectTax= '''jQuery('#select2-selectTaxes-results li').first().trigger({type:'mouseup'})'''
    #Attributes
    ButtonAttributes = '''document.querySelectorAll("[href*='#tab5']")[0].click();'''
    SelectOpenAttributes = '''jQuery('#selectAttributes').select2('open')'''
    SelectAttributes= '''jQuery('#select2-selectAttributes-results li').first().trigger({type:'mouseup'})'''
    #Equipments
    ButtonEquip = '''document.querySelectorAll("[href*='#tab7']")[0].click();'''
    ButtonAddEquip = '''document.querySelectorAll("[href*='/Management/BusinessPartner/_Equipments']")[0].click();'''
    SelectOpenEquip= '''jQuery('#selectEquipments').select2('open')'''
    SelectEquip= '''jQuery('#select2-selectEquipments-results li').first().trigger({type:'mouseup'})'''
    InputEquip= '''document.getElementsByName('Patent')[0].value = "516165165"'''
    #Contact 
    ButtonContact = '''document.querySelectorAll("[href*='#tab8']")[0].click();'''
    ButtonAddContact = '''document.querySelectorAll("[href*='/Management/BusinessPartner/_Contacts']")[0].click();'''
    SelectOpenContact= '''jQuery('#selectContacts').select2('open')'''
    SelectContact= '''jQuery('#select2-selectContacts-results li').first().trigger({type:'mouseup'})'''
    InputContact= '''document.getElementsByName('contactInput')[0].value = "516165165"'''
    #Image
    ButtonIamage= '''document.querySelectorAll("[href*='#tab9']")[0].click();'''
    ButtonAddImage = '''document.querySelectorAll("[href*='/Management/BusinessPartner/_ImageItem']")[0].click();'''
    EditIBP = '''document.querySelectorAll("[href*='/Management/BusinessPartner/Edit']")[0].click();'''
    DeleteBP = '''document.querySelectorAll("[href*='/Management/BusinessPartner/Delete']")[0].click();'''
    ModalDeleteBP = '''document.querySelectorAll(".btn.btn-outline-success")[0].click();'''

    
class CreateSurvey():
    ButtonMenuSurvey = '''document.querySelectorAll("[href*='/dashboard/HumanTalent/Index/MAP-015']")[0].click()'''
    ButtonMenuSurveyAdministrator = '''document.querySelectorAll("[href*='/HumanTalent/Survey/SurveyAdmin/']")[0].click()'''
    ButtonMenuCrearSurvey = '''document.querySelectorAll("[href*='/HumanTalent/Survey/CreateSurvey']")[0].click()'''
    SelectOpenType = '''jQuery('#EntityTypeCode').select2('open')'''
    Select360Survey = '''jQuery('#select2-EntityTypeCode-results li').eq(0).trigger({type:'mouseup'})'''
    SelectFormSurvey = '''jQuery('#select2-EntityTypeCode-results li').eq(1).trigger({type:'mouseup'})'''
    SelectReferenceSurvey = '''jQuery('#select2-EntityTypeCode-results li').eq(2).trigger({type:'mouseup'})'''      
    SelectStatus = '''jQuery('#DocumentTypeStatusCode').select2('open')'''
    SelectOpenStatus = '''jQuery('#select2-DocumentTypeStatusCode-results li').eq(2).trigger({type:'mouseup'})''' 
    ButtonAddQuestion = '''document.querySelector('button[onclick="new CreateSurvey().addQuestionRow();"]').click();'''
    SelectOpenQuestion = '''jQuery('#EntityCodeQuestion').select2('open')'''
    SelectQuestion = '''jQuery('#select2-EntityCodeQuestion-results li').eq(0).trigger({type:'mouseup'})'''
    SelectOpenAnswer = '''jQuery('#EntityCodeAnswer').select2('open')'''
    SelectAnswer = '''jQuery('#select2-EntityCodeAnswer-results li').eq(0).trigger({type:'mouseup'})'''
    ButtonSaveAnswer = '''document.querySelector('button[onclick="new CreateSurvey().getQuestonAndAnswer();"]').click();'''
    ButtonSaveSurvey = '''document.querySelector('button[onclick="new CreateSurvey().saveSurvey();"]').click();'''

class CreateItem():
    ButtonItem = '''window.location.href='/Management/Item';'''
    ButtonItemCreate = '''document.querySelectorAll("[href*='/Management/Item/_ItemForm']")[0].click();'''
    SelectOpenType = '''jQuery('#EntityTypeCode').select2('open')'''
    SelectTypeProduct = '''jQuery('#select2-EntityTypeCode-results li').eq(1).trigger({type:'mouseup'})'''
    SelectTypeService = '''jQuery('#select2-EntityTypeCode-results li').eq(2).trigger({type:'mouseup'})'''
    ButtonIsActive = '''document.querySelector('#IsActive').click();'''
    ButtonForSale = '''document.querySelector('#ForSale').click();'''
    ButtonTaxable = '''document.querySelector('#IsTaxable').click();'''
    ButtonFeatured = '''document.querySelector('#Featured').click();'''
    ButtonImage = '''document.querySelectorAll("[href*='#tab1']")[0].click();'''
    ButtonAddImage = '''document.querySelectorAll("[href*='/Management/Item/_ImageItem']")[0].click();'''
    Image = '''document.getElementById("image").src = "1.png";'''
    #Groups
    ButtonGroup = '''document.querySelectorAll("[href*='#tab2']")[0].click();'''
    ButtonAddGroups = '''document.querySelectorAll("[href*='/Management/Item/_EntityGroups']")[0].click();'''
    SelectOpenGroup = '''jQuery('#selectParentGroups').select2('open')'''
    SelectParentGroup= '''jQuery('#select2-selectParentGroups-results li').first().trigger({type:'mouseup'})'''
    SelectOpenChildGroup = '''jQuery('#selectChildrenGroups').select2('open')'''
    SelectChildGroup= '''jQuery('#select2-selectChildrenGroups-results li').first().trigger({type:'mouseup'})'''
    #PriceList
    ButtonPriceList = '''document.querySelectorAll("[href*='#tab3']")[0].click();'''
    ButtonAddPriceList = '''document.querySelectorAll("[href*='/Management/Item/_PriceList']")[0].click();'''
    SelectOpenPriceList = '''jQuery('#PriceListCode').select2('open')'''
    SelectPriceList= '''jQuery('#select2-PriceListCode-results li').first().trigger({type:'mouseup'})'''
    #Atributes
    ButtonAtributes = '''document.querySelectorAll("[href*='#tab5']")[0].click();'''
    SelectOpenAtributes = '''jQuery('#selectAttributes').select2('open')'''
    SelectAtributes= '''jQuery('#select2-selectAttributes-results li').first().trigger({type:'mouseup'})'''
    #Relations
    ButtonRelations = '''document.querySelectorAll("[href*='#tab6']")[0].click();'''
    ButtonAddRelations = '''document.querySelectorAll("[href*='/Management/Item/_RelatedItems']")[0].click();'''
    SelectOpenRelations = '''jQuery('#selectRelatedParents').select2('open')'''
    SelectRelations= '''jQuery('#select2-selectRelatedParents-results li').first().trigger({type:'mouseup'})'''
    SelectOpenItems = '''jQuery('#selectRelatedItems').select2('open')'''
    SelectItems= '''jQuery('#select2-selectRelatedItems-results li').first().trigger({type:'mouseup'})'''
    #Warehouse
    ButtonWarehouse = '''document.querySelectorAll("[href*='#tab4']")[0].click();'''
    SelectOpenWarehouse = '''jQuery('#selectWarehouse').select2('open')'''
    SelectWarehouse= '''jQuery('#select2-selectWarehouse-results li').first().trigger({type:'mouseup'})'''
    #Index
    EditItem = '''document.querySelectorAll("[href*='/Management/Item/EditItem']")[0].click();'''
    
class CreateDraft():
    ButtonCreate =  '''document.querySelectorAll("[href*='/Documents/Transactions/CreateDraftFormAsync']")[0].click();'''
    GetDraftCode = '''jQuery('#DraftCode')[0].value'''
    SelectOpenClientName = '''document.querySelectorAll('#GetClientCode')[0].click()'''
    SelectOpenClientAddress = '''document.querySelectorAll('#idAddress')[0].click()'''
    SelectOpenProviderName = '''document.querySelectorAll('#customerDir')[0].click()'''
    SelectOpenProviderAddress = '''document.querySelectorAll('#idAddressRecep')[0].click()'''
    ButtonAddItem = '''document.querySelectorAll('#addItem')[0].click()'''
    SaveAll = '''document.querySelector('.btn.btn-outline-info').click()'''
    #Index
    EditDraft = '''document.querySelectorAll("[href*='/Documents/transactions/EditDraftForm']")[0].click();'''
    
class CreateOrder():
    #Index
    TapOrder = '''document.querySelectorAll('#nav-order')[0].click()'''
    ButtonCreate = '''document.querySelectorAll("[href*='/Documents/Transactions/CreateOrderFormAsync']")[0].click();'''
    GetOrderCode = '''jQuery('#OrderCode')[0].value'''
    EditOrder = '''document.querySelectorAll("[href*='/Documents/transactions/EditDraftForm']")[0].click();'''
    
    
class CreateInvoice():
    #Index
    TapInvoice = '''document.querySelectorAll('#nav-invoice')[0].click()'''
    ButtonCreate = '''jQuery('.btn.btn-outline-info')[6].click()'''
    GetInvoiceCode = '''jQuery('#InvoiceCode')[0].value'''
    SelectOpenClient = '''jQuery('#ClientCode').select2('open')'''
    SelectClient = '''jQuery('#select2-ClientCode-results li').first().trigger({type:'mouseup'})'''
    SelectOpenClientAddress = '''jQuery('#ClientAddressCode').select2('open')'''
    SelectClientAddress = '''jQuery('#select2-ClientAddressCode-results li').first().trigger({type:'mouseup'})'''
    SelectOpenProvider = '''jQuery('#ReceiverCode').select2('open')'''
    SelectProvider = '''jQuery('#select2-ReceiverCode-results li').first().trigger({type:'mouseup'})'''
    SelectOpenProviderAddress = '''jQuery('#ReceiverAddressCode').select2('open')'''
    SelectProviderAddress = '''jQuery('#select2-ReceiverAddressCode-results li').first().trigger({type:'mouseup'})'''
    AddItem = '''document.querySelectorAll('.btn.btn-outline-info.waves-effect.waves-light.float-right.m-l-5')[0].click()'''
    SaveInvoice = '''document.querySelector('button[onclick="new Invoice().saveRecord()"]').click();'''
    EditInvoice = '''document.querySelectorAll("[href*='/Documents/Transactions/Edit']")[0].click();'''
    
class CreateGroup():
    ButtonEntityGroup = '''document.querySelectorAll("[href*='/settings/entitygroup']")[0].click();'''
    ButtonCreateEntityGroup = '''document.querySelectorAll("[href*='/Settings/EntityGroup/CreateGroupFormAsync']")[0].click();'''
    SelectOpenEntityType = '''jQuery('#ListEntityTypes').select2('open')'''
    SelectEntityType = '''jQuery('#select2-ListEntityTypes-results li').last().trigger({type:'mouseup'})'''
    SelectOpenFatherCode = '''jQuery('#ListParents').select2('open')'''
    SelectFatherCode = '''jQuery('#select2-ListParents-results li').last().trigger({type:'mouseup'})'''
    DeleteGroup = '''document.querySelectorAll("[href*='/Settings/EntityGroup/DeleteGroupFormAsync']")[0].click();'''

class CreateWareHouse():
    ButtonWarehouse = '''document.querySelectorAll("[href*='/Management/WareHouse']")[0].click();'''
    ButtonCreateWarehouse = '''document.querySelectorAll("[href*='/Management/Warehouse/Form']")[0].click();'''
    SelectClientTypeEntityOpen = '''jQuery('#EntityTypeCode').select2('open')'''
    SelectClientTypeEntity = '''jQuery('#select2-EntityTypeCode-results li').first().trigger({type:'mouseup'})'''