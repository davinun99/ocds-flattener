import sys
sys.path.append('./src')
import helpers
import scripts.guarantees_obligations as guarantees_obligations
# import scripts.OLD_contracts_investmentprojects_id as OLD_contracts_investmentprojects_id
import scripts.contracts_amendments_amendsAmount as contracts_amendments_amendsAmount
import scripts.contracts_amendments_count as contracts_amendments_count
import scripts.contracts_implementation_purchaseOrders_count as contracts_implementation_purchaseOrders_count
import scripts.contracts_implementation_transactions_count as contracts_implementation_transactions_count
import scripts.contracts_documents_DocumentTypeDetails as contracts_documents_DocumentTypeDetails
import scripts.contracts_value_amount as contracts_value_amount
import scripts.contracts_status as contracts_status
import scripts.contracts_statusDetails as contracts_statusDetails
import scripts.awards_documents_documentTypeDetails as awards_documents_documentTypeDetails
import dynamicScripts.awards_suppliers_id as awards_suppliers_id
import scripts.awards_value_amount as awards_value_amount
import scripts.awards_status as awards_status
import scripts.awards_statusDetails as awards_statusDetails
import scripts.tender_coveredBy as tender_coveredBy
import col_scripts.tender_criteria_id as tender_criteria_id
import col_scripts.tender_enquiries as tender_enquiries
import col_scripts.tender_lots as tender_lots
import dynamicScripts.tender_notifiedSuppliers_id as tender_notifiedSuppliers_id
import col_scripts.tender_documents_documentTypeDetails as tender_documents_documentTypeDetails
import dynamicScripts.tender_tenderers_id as tender_tenderers_id

import tender_items_classification.N5_tender_items_classification_id as N5_tender_items_classification_id
import tender_items_classification.N4_tender_items_classification_id as N4_tender_items_classification_id
import tender_items_classification.N3_tender_items_classification_id as N3_tender_items_classification_id
import tender_items_classification.N2_tender_items_classification_id as N2_tender_items_classification_id
import tender_items_classification.N1_tender_items_classification_id as N1_tender_items_classification_id
import tender_items_classification.N1_1_tender_items_classification_id as N1_1_tender_items_classification_id

import planning_items_classification.N4_planning_items_classification_id as N4_planning_items_classification_id
import planning_items_classification.N3_planning_items_classification_id as N3_planning_items_classification_id
import planning_items_classification.N2_planning_items_classification_id as N2_planning_items_classification_id
import planning_items_classification.N1_planning_items_classification_id as N1_planning_items_classification_id
import planning_items_classification.N1_1_planning_items_classification_id as N1_1_planning_items_classification_id

import col_scripts.parties_details_entityType as parties_details_entityType
import col_scripts.parties_details_legalEntityTypeDetail as parties_details_legalEntityTypeDetail
import col_scripts.parties_roles as parties_roles

import quartiles_structured.tender_procurementMethodDetails as tender_procurementMethodDetails
import quartiles_structured.tender_procuringEntity_id as tender_procuringEntity_id
import quartiles_structured.tender_procuringEntity_name as tender_procuringEntity_name
import quartiles_structured.tender_procurementIntention_procuringEntity_id as tender_procurementIntention_procuringEntity_id
import quartiles_structured.tender_procurementIntention_procuringEntity_name as tender_procurementIntention_procuringEntity_name
import quartiles_structured.buyer_id as buyer_id
import quartiles_structured.buyer_name as buyer_name
import quartiles_structured.secondStage_id as secondStage_id
import quartiles_structured.tender_eligibilityCriteria as tender_eligibilityCriteria
import quartiles_structured.tender_mainProcurementCategoryDetails as tender_mainProcurementCategoryDetails
import quartiles_structured.tender_submissionMethodDetails as tender_submissionMethodDetails
import quartiles_structured.tender_procurementIntention_category as tender_procurementIntention_category
import quartiles_structured.contacts_investmentprojects_id as contacts_investmentprojects_id

# function to print a name for every column when we are splitting a list column
def obtain_column_names(column_title, amount):
	result = ""
	for i in range(1,amount+1):
		result += column_title + "_" + str(i)
	return result

# function to the title 4 times for quartiles
def name_to_quartiles(column_title):
	result = ""
	for i in range(1,5):
		result += column_title + " q" + str(i)
	return result

def main(arguments):
	query = """
SELECT
	r.ocid,
	data['compiledRelease']['id'] as "id",
	data['compiledRelease']['tender']['id'] as "tender.id",
	data['compiledRelease']['tender']['title'] as "tender.title",
	data['compiledRelease']['tender']['status'] as "tender.status",
	data['compiledRelease']['tender']['awardCriteria'] as "tender.awardCriteria",
	data['compiledRelease']['tender']['awardCriteriaDetails'] as "tender.awardCriteriaDetails",
	data['compiledRelease']['tender']['bidOpening']['date'] as "tender.bidOpening.date",
	data['compiledRelease']['tender']['bidOpening']['address']['streetAddress'] as "tender.bidOpening.address.streetAddress",
	data['compiledRelease']['tender']['submissionMethodDetails'] as "tender.submissionMethodDetails",
	data['compiledRelease']['tender']['eligibilityCriteria'] as "tender.eligibilityCriteria",
	data['compiledRelease']['tender']['statusDetails'] as "tender.statusDetails",
	data['compiledRelease']['tender']['enquiriesAddress']['streetAddress']as "tender.enquiriesAddress.streetAddress",
	data['compiledRelease']['tender']['mainProcurementCategoryDetails'] as "tender.mainProcurementCategoryDetails",
	data['compiledRelease']['tender']['hasEnquiries'] as "tender.hasEnquiries",
	data['compiledRelease']['tender']['value']['amount'] as "tender.value.amount",
	data['compiledRelease']['tender']['value']['currency'] as "tender.value.currency",
	data['compiledRelease']['tender']['datePublished'] as "tender.datePublished",
	data['compiledRelease']['tender']['tenderPeriod']['startDate'] as "tender.tenderPeriod.startDate",
	data['compiledRelease']['tender']['tenderPeriod']['endDate'] as "tender.tenderPeriod.endDate",
	data['compiledRelease']['tender']['tenderPeriod']['durationInDays'] as "tender.tenderPeriod.durationInDays",
	data['compiledRelease']['tender']['awardPeriod']['startDate'] as "tender.awardPeriod.startDate",
	data['compiledRelease']['tender']['enquiryPeriod']['endDate'] as "tender.enquiryPeriod.endDate",
	data['compiledRelease']['tender']['enquiryPeriod']['startDate'] as "tender.enquiryPeriod.startDate",
	data['compiledRelease']['tender']['enquiryPeriod']['durationInDays'] as "tender.enquiryPeriod.durationInDays",
	data['compiledRelease']['tender']['mainProcurementCategory'] as "tender.mainProcurementCategory",	
	data['compiledRelease']['tender']['procurementMethod'] as "tender.procurementMethod",
	data['compiledRelease']['tender']['procurementMethodDetails'] as "tender.procurementMethodDetails",	
	data['compiledRelease']['tender']['procuringEntity']['id'] as "tender.procuringEntity.id",
	data['compiledRelease']['tender']['procuringEntity']['name'] as "tender.procuringEntity.name",
	data['compiledRelease']['tender']['numberOfTenderers'] as "tender.numberOfTenderers",
	data['compiledRelease']['language'] as "language",	
	data['compiledRelease']['ocid'] as "ocid",
	data['compiledRelease']['date'] as "date",
	data['compiledRelease']['initiationType'] as "initiationType",
	data['compiledRelease']['buyer']['id'] as "buyer.id",
	data['compiledRelease']['buyer']['name'] as "buyer.name",
	data['compiledRelease']['planning']['identifier'] as "planning.identifier",
	data['compiledRelease']['planning']['estimatedDate'] as "planning.estimatedDate",
	data['compiledRelease']['planning']['budget']['description'] as "planning.budget.description",
	data['compiledRelease']['planning']['budget']['amount']['currency'] as "planning.budget.amount.currency",
	data['compiledRelease']['planning']['budget']['amount']['amount'] as "planning.budget.amount.amount",
	data['compiledRelease']['tag'] as "tag",
	data['compiledRelease']['tender']['techniques']['hasElectronicAuction'] as "tender.techniques.hasElectronicAuction",
	data['compiledRelease']['tender']['contractPeriod']['durationInDays'] as "tender.contractPeriod.durationInDays",
	data['compiledRelease']['tender']['contractPeriod']['maxExtentDate'] as "tender.contractPeriod.maxExtentDate",
	data['compiledRelease']['tender']['procurementMethodRationale'] as "tender.procurementMethodRationale",
	data['compiledRelease']['tender']['procurementIntention']['id'] as "tender.procurementIntention.id",
	data['compiledRelease']['tender']['procurementIntention']['uri'] as "tender.procurementIntention.uri",
	data['compiledRelease']['tender']['procurementIntention']['rationale'] as "tender.procurementIntention.rationale",
	data['compiledRelease']['tender']['procurementIntention']['category'] as "tender.procurementIntention.category",
	data['compiledRelease']['tender']['procurementIntention']['title'] as "tender.procurementIntention.title",
	data['compiledRelease']['tender']['procurementIntention']['description'] as "tender.procurementIntention.description",
	data['compiledRelease']['tender']['procurementIntention']['startDate'] as "tender.procurementIntention.startDate",
	data['compiledRelease']['tender']['procurementIntention']['publishedDate'] as "tender.procurementIntention.publishedDate",
	data['compiledRelease']['tender']['procurementIntention']['procuringEntity']['id'] as "tender.procurementIntention.procuringEntity.id",
	data['compiledRelease']['tender']['procurementIntention']['procuringEntity']['name'] as "tender.procurementIntention.procuringEntity.name",
	data['compiledRelease']['tender']['procurementIntention']['status'] as "tender.procurementIntention.status",
	data['compiledRelease']['tender']['procurementIntention']['statusDetails'] as "tender.procurementIntention.statusDetails",
	data['compiledRelease']['secondStage']['id'] as "secondStage.id",
	data['compiledRelease']['tender']['techniques']['hasFrameworkAgreement'] as "tender.techniques.hasFrameworkAgreement",
	data['compiledRelease']['tender']['contractPeriod']['startDate'] as "tender.contractPeriod.startDate",
	data['compiledRelease']['tender']['contractPeriod']['endDate'] as "tender.contractPeriod.endDate",
	COALESCE(jsonb_array_length(data['compiledRelease']['tender']['lots']), 0) as "tender.lots.count",  --remove later
	COALESCE(jsonb_array_length(data['compiledRelease']['tender']['enquiries']), 0) as "tender.enquiries.count", --remove later
	COALESCE(jsonb_array_length(data['compiledRelease']['awards']), 0) as "awards.count",
	COALESCE(jsonb_array_length(data['compiledRelease']['contracts']), 0) as "contracts.count",
	data['compiledRelease']['contracts'] as "contracts", -- 67
	data['compiledRelease']['awards'] as "awards", --68
	data['compiledRelease']['tender']['coveredBy'] as "tender.coveredBy", --69
	data['compiledRelease']['tender'] as "tender", --70
	data['compiledRelease']['planning'] as "planning", --71
	data['compiledRelease']['parties'] as "parties", --72
	data['compiledRelease']['complaints'] as "complaints", --73
	COALESCE(jsonb_array_length(data['compiledRelease']['complaints']), 0) as "complaints.count", --74
	data['compiledRelease']['buyer'] as "buyer", --75
	data['compiledRelease']['secondStage'] as "secondStage" --76
FROM RECORD r join data d on d.id = r.data_id
	"""
	print(f'ocid;;;id;;;tender.id;;;tender.title;;;tender.status;;;tender.awardCriteria;;;tender.awardCriteriaDetails;;;tender.bidOpening.date;;;tender.bidOpening.address.streetAddress;;;tender.submissionMethodDetails;;;tender.eligibilityCriteria;;;tender.statusDetails;;;tender.enquiriesAddress.streetAddress;;;tender.mainProcurementCategoryDetails;;;tender.hasEnquiries;;;tender.value.amount;;;tender.value.currency;;;tender.datePublished;;;tender.tenderPeriod.startDate;;;tender.tenderPeriod.endDate;;;tender.tenderPeriod.durationInDays;;;tender.awardPeriod.startDate;;;tender.enquiryPeriod.endDate;;;tender.enquiryPeriod.startDate;;;tender.enquiryPeriod.durationInDays;;;tender.mainProcurementCategory;;;tender.procurementMethod;;;tender.procurementMethodDetails;;;tender.procuringEntity.id;;;tender.procuringEntity.name;;;tender.numberOfTenderers;;;language;;;ocid;;;date;;;initiationType;;;buyer.id;;;buyer.name;;;planning.identifier;;;planning.estimatedDate;;;planning.budget.description;;;planning.budget.amount.currency;;;planning.budget.amount.amount;;;tag;;;tender.techniques.hasElectronicAuction;;;tender.contractPeriod.durationInDays;;;tender.contractPeriod.maxExtentDate;;;tender.procurementMethodRationale;;;tender.procurementIntention.id;;;tender.procurementIntention.uri;;;tender.procurementIntention.rationale;;;tender.procurementIntention.category;;;tender.procurementIntention.title;;;tender.procurementIntention.description;;;tender.procurementIntention.startDate;;;tender.procurementIntention.publishedDate;;;tender.procurementIntention.procuringEntity.id;;;tender.procurementIntention.procuringEntity.name;;;tender.procurementIntention.status;;;tender.procurementIntention.statusDetails;;;secondStage.id;;;tender.techniques.hasFrameworkAgreement;;;tender.contractPeriod.startDate;;;tender.contractPeriod.endDate;;;tender.lots.count;;;tender.enquiries.count;;;awards.count;;;contracts.count', end='')
	print(obtain_column_names(';;;contracts.guarantees.obligations',18)+name_to_quartiles(';;;contracts.investmentProjects.id')+';;;contracts.amendments.amendsAmount_pyg;;;contracts.amendments.amendsAmount_usd;;;contracts.amendments.count;;;contracts.implementation.purchaseOrders.count;;;contracts.implementation.transactions.count'+obtain_column_names(';;;contracts.documents.DocumentTypeDetails',12), end='')
	print(';;;contracts.value.amount_pyg;;;contracts.value.amount_usd'+obtain_column_names(';;;contracts.status',4)+obtain_column_names(';;;contracts.statusDetails',9)+obtain_column_names(';;;awards.documents.DocumentTypeDetails',21)+';;;awards.suppliers.id q1;;;awards.suppliers.id q2;;;awards.suppliers.id q3;;;awards.suppliers.id q4;;;awards.value.amount_pyg;;;awards.value.amount_usd', end='')
	print(obtain_column_names(';;;awards.status',4)+obtain_column_names(';;;awards.statusDetails',11)+obtain_column_names(';;;tender.coveredBy',8)+';;;tender.notifiedSuppliers.id q1;;;tender.notifiedSuppliers.id q2;;;tender.notifiedSuppliers.id q3;;;tender.notifiedSuppliers.id q4;;;tender.tenderers.id q1;;;tender.tenderers.id q2;;;tender.tenderers.id q3;;;tender.tenderers.id q4', end='')
	print(';;;tender.items.classification.id.n5 q1;;;tender.items.classification.id.n5 q2;;;tender.items.classification.id.n5 q3;;;tender.items.classification.id.n5 q4;;;tender.items.classification.id.n4 q1;;;tender.items.classification.id.n4 q2;;;tender.items.classification.id.n4 q3;;;tender.items.classification.id.n4 q4;;;tender.items.classification.id.n3 q1;;;tender.items.classification.id.n3 q2;;;tender.items.classification.id.n3 q3;;;tender.items.classification.id.n3 q4'+obtain_column_names(';;;tender.items.classification.id.n2',20)+obtain_column_names(';;;tender.items.classification.id.n1',11)+obtain_column_names(';;;tender.items.classification.id.n1_1',57)+';;;tender.criteria.id;;;tender.enquiries total;;;tender.enquiries respondidos;;;tender.enquiries porcentaje;;;tender.lots'+obtain_column_names(';;;tender.documents.documentTypeDetails',13), end='')
	print(';;;planning.items.classification.id.n4 q1;;;planning.items.classification.id.n4 q2;;;planning.items.classification.id.n4 q3;;;planning.items.classification.id.n4 q4;;;planning.items.classification.id.n3 q1;;;planning.items.classification.id.n3 q2;;;planning.items.classification.id.n3 q3;;;planning.items.classification.id.n3 q4'+obtain_column_names(';;;planning.items.classification.id.n2',44)+obtain_column_names(';;;planning.items.classification.id.n1',15)+obtain_column_names(';;;planning.items.classification.id.n1_1',57), end='')
	print(obtain_column_names(';;;parties.details.EntityType candidate',4)+obtain_column_names(';;;parties.details.EntityType enquirer',4)+obtain_column_names(';;;parties.details.EntityType payer',4)+obtain_column_names(';;;parties.details.EntityType payee',4)+obtain_column_names(';;;parties.details.EntityType supplier',4)+obtain_column_names(';;;parties.details.EntityType procuringEntity',4)+obtain_column_names(';;;parties.details.EntityType buyer',4)+obtain_column_names(';;;parties.details.EntityType tenderer',4)+obtain_column_names(';;;parties.details.EntityType notifiedSupplier',4)+obtain_column_names(';;;parties.details.legalEntityTypeDetail candidate',24)+obtain_column_names(';;;parties.details.legalEntityTypeDetail enquirer',24)+obtain_column_names(';;;parties.details.legalEntityTypeDetail payer',24)+obtain_column_names(';;;parties.details.legalEntityTypeDetail payee',24)+obtain_column_names(';;;parties.details.legalEntityTypeDetail supplier',24)+obtain_column_names(';;;parties.details.legalEntityTypeDetail procuringEntity',24)+obtain_column_names(';;;parties.details.legalEntityTypeDetail buyer',24)+obtain_column_names(';;;parties.details.legalEntityTypeDetail tenderer',24)+obtain_column_names(';;;parties.details.legalEntityTypeDetail notifiedSupplier',24)+';;;parties.roles candidate q1;;;parties.roles candidate q2;;;parties.roles candidate q3;;;parties.roles candidate q4;;;parties.roles enquirer q1;;;parties.roles enquirer q2;;;parties.roles enquirer q3;;;parties.roles enquirer q4;;;parties.roles payer q1;;;parties.roles payer q2;;;parties.roles payer q3;;;parties.roles payer q4;;;parties.roles payee q1;;;parties.roles payee q2;;;parties.roles payee q3;;;parties.roles payee q4;;;parties.roles supplier q1;;;parties.roles supplier q2;;;parties.roles supplier q3;;;parties.roles supplier q4;;;parties.roles procuringEntity q1;;;parties.roles procuringEntity q2;;;parties.roles procuringEntity q3;;;parties.roles procuringEntity q4;;;parties.roles buyer q1;;;parties.roles buyer q2;;;parties.roles buyer q3;;;parties.roles buyer q4;;;parties.roles tenderer q1;;;parties.roles tenderer q2;;;parties.roles tenderer q3;;;parties.roles tenderer q4;;;parties.roles notifiedSupplier q1;;;parties.roles notifiedSupplier q2;;;parties.roles notifiedSupplier q3;;;parties.roles notifiedSupplier q4', end='')
	print(name_to_quartiles(';;;tender.procurementMethodDetails')+name_to_quartiles(';;;tender.procuringEntity.id')+name_to_quartiles(';;;tender.procuringEntity.name')+name_to_quartiles(';;;tender.procurementIntention.procuringEntity.id')+name_to_quartiles(';;;tender.procurementIntention.procuringEntity.name')+name_to_quartiles(';;;buyer.id')+name_to_quartiles(';;;buyer.name')+name_to_quartiles(';;;secondStage.id')+name_to_quartiles(';;;tender.eligibilityCriteria')+name_to_quartiles(';;;tender.mainProcurementCategoryDetails')+name_to_quartiles(';;;tender.submissionMethodDetails')+name_to_quartiles(';;;tender.ProcurementIntentionCategory'), end='')
	print(';;;has_complaint')

	rows = helpers.get_rows(query)
	AwardSuppliers = awards_suppliers_id.AwardSuppliers(rows, 68)
	TenderNotifiedSuppliers = tender_notifiedSuppliers_id.NotifiedSuppliers(rows, 70)
	TenderTenderers = tender_tenderers_id.TenderTenderers(rows, 70)
	N5TenderItemsClass = N5_tender_items_classification_id.N5TenderItemsClassification(rows, 70)
	N4TenderItemsClass = N4_tender_items_classification_id.N4TenderItemsClassification(rows, 70)
	N3TenderItemsClass = N3_tender_items_classification_id.N3TenderItemsClassification(rows, 70)
	N2TenderItemsClass = N2_tender_items_classification_id.N2TenderItemsClassification(rows, 70)
	N1TenderItemsClass = N1_tender_items_classification_id.N1TenderItemsClassification(rows, 70)
	N1_1TenderItemsClass = N1_1_tender_items_classification_id.N1_1TenderItemsClassification(rows, 70)
	TenderDocumentsDocumentTypeDetail = tender_documents_documentTypeDetails.TenderDocumentsDocumentTypeDetail(rows, 70)
	N4PlanningItemsClass = N4_planning_items_classification_id.N4PlanningItemsClassification(rows, 71)
	N3PlanningItemsClass = N3_planning_items_classification_id.N3PlanningItemsClassification(rows, 71)
	N2PlanningItemsClass = N2_planning_items_classification_id.N2PlanningItemsClassification(rows, 71)
	N1PlanningItemsClass = N1_planning_items_classification_id.N1PlanningItemsClassification(rows, 71)
	N1_1PlanningItemsClass = N1_1_planning_items_classification_id.N1_1PlanningItemsClassification(rows, 71)
	PartiesRoles = parties_roles.PartiesRoles(rows, 72)
	TenderProcurementMethodDetails = tender_procurementMethodDetails.TenderProcurementMethodDetails(rows, 70)
	TenderProcuringEntityId = tender_procuringEntity_id.TenderProcuringEntityId(rows, 70)
	TenderProcuringEntityName = tender_procuringEntity_name.TenderProcuringEntityName(rows, 70)
	TenderProcurementIntentionProcuringEntityId = tender_procurementIntention_procuringEntity_id.TenderProcurementIntentionProcuringEntityId(rows, 70)
	TenderProcurementIntentionProcuringEntityName = tender_procurementIntention_procuringEntity_name.TenderProcurementIntentionProcuringEntityName(rows, 70)
	BuyerId = buyer_id.BuyerId(rows, 75)
	BuyerName = buyer_name.BuyerName(rows, 75)
	SecondStageId = secondStage_id.SecondStageId(rows, 76)
	TenderEligibilityCriteria = tender_eligibilityCriteria.TenderEligibilityCriteria(rows, 70)
	TenderMainProcurementCategoryDetails = tender_mainProcurementCategoryDetails.TenderMainProcurementCategoryDetails(rows, 70)
	TendersubmissionMethodDetails = tender_submissionMethodDetails.TendersubmissionMethodDetails(rows, 70)
	TenderProcurementIntentionCategory = tender_procurementIntention_category.TenderProcurementIntentionCategory(rows, 70)
	InvestmentProjectsId = contacts_investmentprojects_id.InvestmentProjectsId(rows, 67)
	
	for row in rows:
		line = ''
		try:
			for i in range(67):
				if i == 0:
					line += row[i]
					pass
				elif i < 67:  #(67 direct from db)
					if i == 3 or i == 39: # tender title and budget description
						line += f';;;"{row[i]}"'
					else:
						line += f';;;{row[i]}'
				## PROCESS SOME ROWS
			res67 = guarantees_obligations.process_row(row, 67)
			res68 = InvestmentProjectsId.process_row(row, 67)
			res69 = contracts_amendments_amendsAmount.process_row(row, 67)
			res70 = contracts_amendments_count.process_row(row, 67)
			res71 = contracts_implementation_purchaseOrders_count.process_row(row, 67)
			res72 = contracts_implementation_transactions_count.process_row(row, 67)
			res73 = contracts_documents_DocumentTypeDetails.process_row(row, 67)
			res74 = contracts_value_amount.process_row(row, 67)
			res75 = contracts_status.process_row(row, 67)
			res76 = contracts_statusDetails.process_row(row, 67)
			line += f';;;{res67};;;{res68};;;{res69[0]};;;{res69[1]};;;{res70};;;{res71};;;{res72};;;{res73};;;{res74[0]};;;{res74[1]};;;{res75};;;{res76}'
			
			res77 = awards_documents_documentTypeDetails.process_row(row, 68)
			res78 = AwardSuppliers.process_row(row, 68)
			res79 = awards_value_amount.process_row(row, 68)
			res80 = awards_status.process_row(row, 68)
			res81 = awards_statusDetails.process_row(row, 68)
			line += f';;;{res77};;;{res78};;;{res79[0]};;;{res79[1]};;;{res80};;;{res81}'
				
			res82 = tender_coveredBy.process_row(row, 69)
			line += f';;;{res82}'

			res83 = TenderNotifiedSuppliers.process_row(row, 70)
			res84 = TenderTenderers.process_row(row, 70)
			res85 = N5TenderItemsClass.process_row(row, 70)
			res86 = N4TenderItemsClass.process_row(row, 70)
			res87 = N3TenderItemsClass.process_row(row, 70)
			res88 = N2TenderItemsClass.process_row(row, 70)
			res89 = N1TenderItemsClass.process_row(row, 70)
			res90 = N1_1TenderItemsClass.process_row(row, 70)
			res96 = tender_criteria_id.process_row(row, 70)
			res97 = tender_enquiries.process_row(row, 70)
			res98 = tender_lots.process_row(row, 70)
			res99 = TenderDocumentsDocumentTypeDetail.process_row(row, 70)

			line += f';;;{res83};;;{res84};;;{res85};;;{res86};;;{res87};;;{res88};;;{res89};;;{res90};;;{res96};;;{res97};;;{res98};;;{res99}'

			res91 = N4PlanningItemsClass.process_row(row, 71)
			res92 = N3PlanningItemsClass.process_row(row, 71)
			res93 = N2PlanningItemsClass.process_row(row, 71)
			res94 = N1PlanningItemsClass.process_row(row, 71)
			res95 = N1_1PlanningItemsClass.process_row(row, 71)
			# print(f';;;{res91};;;{res92};;;{res93};;;{res94};;;{res95}', end='')
			line += f';;;{res91};;;{res92};;;{res93};;;{res94};;;{res95}'
			
			res100 = parties_details_entityType.process_row(row, 72)
			res101 = parties_details_legalEntityTypeDetail.process_row(row, 72)
			res102 = PartiesRoles.process_row(row, 72)
			# print(f';;;{res100};;;{res101};;;{res102};;;{res103}', end='')
			line += f';;;{res100};;;{res101};;;{res102}'

			res104 = TenderProcurementMethodDetails.process_row(row, 70)
			res105 = TenderProcuringEntityId.process_row(row, 70)
			res106 = TenderProcuringEntityName.process_row(row, 70)
			res107 = TenderProcurementIntentionProcuringEntityId.process_row(row, 70)
			res108 = TenderProcurementIntentionProcuringEntityName.process_row(row, 70)
			res109 = BuyerId.process_row(row, 75)
			res110 = BuyerName.process_row(row, 75)
			res111 = SecondStageId.process_row(row, 76)
			res112 = TenderEligibilityCriteria.process_row(row, 70)
			res113 = TenderMainProcurementCategoryDetails.process_row(row, 70)
			res114 = TendersubmissionMethodDetails.process_row(row, 70)
			res115 = TenderProcurementIntentionCategory.process_row(row, 70)
			line += f';;;{res104};;;{res105};;;{res106};;;{res107};;;{res108};;;{res109};;;{res110};;;{res111};;;{res112};;;{res113};;;{res114};;;{res115}'

			res103 = int(row[74]) > 0 # CAMBIAR AL ÚLTIMO ESTA COLUMNA PORQUE ES LA COLUMNA OBJETIVO
			line += f';;;{res103}'

			line = line.replace("\n", " ")
		except Exception as ex:
			print('Exception:', ex)
			print(ex.with_traceback(None))

		print(line)

		n_complaints = int(row[74])
		for i in range(n_complaints - 1):
			print(line)
		# except Exception as ex:
		# 	print('\nException while processing row', ex)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))