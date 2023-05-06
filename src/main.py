import sys
sys.path.append('./src')
import helpers
import scripts.guarantees_obligations as guarantees_obligations
import scripts.contracts_investmentprojects_id as contracts_investmentprojects_id
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
# tender.criteria.id
import dynamicScripts.tender_notifiedSuppliers_id as tender_notifiedSuppliers_id
# import scripts.tender
# tender.documents.DocumentTypeDetails
import dynamicScripts.tender_tenderers_id as tender_tenderers_id

import tender_items_classification.N5_tender_items_classification_id as N5_tender_items_classification_id
import tender_items_classification.N4_tender_items_classification_id as N4_tender_items_classification_id
import tender_items_classification.N3_tender_items_classification_id as N3_tender_items_classification_id
import tender_items_classification.N2_tender_items_classification_id as N2_tender_items_classification_id
import tender_items_classification.N1_tender_items_classification_id as N1_tender_items_classification_id
import tender_items_classification.N1_1_tender_items_classification_id as N1_1_tender_items_classification_id

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
	COALESCE(jsonb_array_length(data['compiledRelease']['tender']['lots']), 0) as "tender.lots.count",
	COALESCE(jsonb_array_length(data['compiledRelease']['tender']['enquiries']), 0) as "tender.enquiries.count",
	COALESCE(jsonb_array_length(data['compiledRelease']['awards']), 0) as "awards.count",
	COALESCE(jsonb_array_length(data['compiledRelease']['contracts']), 0) as "contracts.count",
	data['compiledRelease']['contracts'] as "contracts",
	-- 67
	data['compiledRelease']['awards'] as "awards"
FROM RECORD r join data d on d.id = r.data_id 
	"""
	print(f'ocid;;;id;;;tender.id;;;tender.title;;;tender.status;;;tender.awardCriteria;;;tender.awardCriteriaDetails;;;tender.bidOpening.date;;;tender.bidOpening.address.streetAddress;;;tender.submissionMethodDetails;;;tender.eligibilityCriteria;;;tender.statusDetails;;;tender.enquiriesAddress.streetAddress;;;tender.mainProcurementCategoryDetails;;;tender.hasEnquiries;;;tender.value.amount;;;tender.value.currency;;;tender.datePublished;;;tender.tenderPeriod.startDate;;;tender.tenderPeriod.endDate;;;tender.tenderPeriod.durationInDays;;;tender.awardPeriod.startDate;;;tender.enquiryPeriod.endDate;;;tender.enquiryPeriod.startDate;;;tender.enquiryPeriod.durationInDays;;;tender.mainProcurementCategory;;;tender.procurementMethod;;;tender.procurementMethodDetails;;;tender.procuringEntity.id;;;tender.procuringEntity.name;;;tender.numberOfTenderers;;;language;;;ocid;;;date;;;initiationType;;;buyer.id;;;buyer.name;;;planning.identifier;;;planning.estimatedDate;;;planning.budget.description;;;planning.budget.amount.currency;;;planning.budget.amount.amount;;;tag;;;tender.techniques.hasElectronicAuction;;;tender.contractPeriod.durationInDays;;;tender.contractPeriod.maxExtentDate;;;tender.procurementMethodRationale;;;tender.procurementIntention.id;;;tender.procurementIntention.uri;;;tender.procurementIntention.rationale;;;tender.procurementIntention.category;;;tender.procurementIntention.title;;;tender.procurementIntention.description;;;tender.procurementIntention.startDate;;;tender.procurementIntention.publishedDate;;;tender.procurementIntention.procuringEntity.id;;;tender.procurementIntention.procuringEntity.name;;;tender.procurementIntention.status;;;tender.procurementIntention.statusDetails;;;secondStage.id;;;tender.techniques.hasFrameworkAgreement;;;tender.contractPeriod.startDate;;;tender.contractPeriod.endDate;;;tender.lots.count;;;tender.enquiries.count;;;awards.count;;;contracts.count', end='')
	print(';;;contracts.guarantees.obligations;;;contracts.investmentProjects.id;;;contracts.amendments.amendsAmount_pyg;;;contracts.amendments.amendsAmount_usd;;;contracts.implementation.purchaseOrders.count;;;contracts.implementation.transactions.count;;;contracts.documents.DocumentTypeDetails', end='')
	print(';;;contracts.value.amount_pyg;;;contracts.value.amount_pyg;;;contracts.status;;;contracts.statusDetails;;;awards.documents.DocumentTypeDetails;;;awards.suppliers.id;;;awards.value.amount_pyg;;;awards.value.amount_usd')
	
	rows = helpers.get_rows(query)
	AwardSuppliers = awards_suppliers_id.AwardSuppliers(rows)

	for row in rows:
		# idArr = process_row(row)
		for i in range(len(row)):
			if i == 0:
				print(row[i], end='')
			elif i < 67:  #(67 direct from db)
				print(f';;;{row[i]}', end='')
			## PROCESS SOME ROWS
			elif i == 67:
				res67 = guarantees_obligations.process_row(row, 67)
				res68 = contracts_investmentprojects_id.process_row(row, 67)
				res69 = contracts_amendments_amendsAmount.process_row(row, 67)
				res70 = contracts_amendments_count.process_row(row, 67)
				res71 = contracts_implementation_purchaseOrders_count.process_row(row, 67)
				res72 = contracts_implementation_transactions_count.process_row(row, 67)
				res73 = contracts_documents_DocumentTypeDetails.process_row(row, 67)
				res74 = contracts_value_amount.process_row(row, 67)
				res75 = contracts_status.process_row(row, 67)
				res76 = contracts_statusDetails.process_row(row, 67)
				res77 = awards_documents_documentTypeDetails.process_row(row, 68)
				res78 = AwardSuppliers.process_row(row, 68)
				res79 = awards_value_amount.process_row(row, 68)
				print(f';;;{res67};;;{res68};;;{res69[0]};;;{res69[1]};;;{res70};;;{res71};;;{res72};;;{res73};;;{res74[0]};;;{res74[1]};;;{res75};;;{res76};;;{res77};;;{res78};;;{res79[0]};;;{res79[1]}', end='')
			# elif i == 68:
			# df_total = pd.read_csv('result.csv', sep=';;;', index_col=False)
		print('')

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))