from graphene_django import DjangoObjectType
import graphene
from graphene import relay
from django.contrib.auth.models import User as UserModel
from .models import PatientDemograph as PatientModel, Contact as ContactModel, Insurance as InsuranceModel, InsuranceSchemes as InsuranceSchemeModel
from .models import LogAppointment as LogAppointmentModel
from .models import PatientQueue as PatientQueueModel
from .models import Departments as DepartmentModel
from .models import CostCentre as CostCentreModel
from .models import Room as RoomModel
from .models import RoomType as RoomTypeModel
from .models import Ward as WardModel
from .models import Bed as BedModel
from .models import Procedure as ProcedureModel
from .models import ProcedureCategory as ProcedureCategoryModel
from .models import PatientProcedure as PatientProcedureModel
from .models import PatientProcedureNote as PatientProcedureNoteModel

class User(DjangoObjectType):
	class Meta:
		model = UserModel

class PatientDemographNode(DjangoObjectType):
	class Meta:
		model = PatientModel
		interfaces = (relay.Node, )

	@classmethod
	def get_node(cls, info, id):
		return PatientModel.objects.get(pk=id)


class LogAppointmentNode(DjangoObjectType):
	class Meta:
		model = LogAppointmentModel
		interfaces = (relay.Node, )

class PatientQueue(DjangoObjectType):
	class Meta:
		model = PatientQueueModel

class InsuranceSchemeNode(DjangoObjectType):
	class Meta:
		model = InsuranceSchemeModel
		interfaces = (relay.Node, )

	@classmethod
	def get_node(cls, info, id):
		return InsuranceSchemeModel.objects.get(pk=id)

class ContactNode(DjangoObjectType):
	class Meta:
		model = ContactModel
		interfaces = (relay.Node, )
	@classmethod
	def get_node(cls, info, id):
		return ContactModel.objects.get(pk=id)

class InsuranceNode(DjangoObjectType):
	class Meta:
		model = InsuranceModel
		interfaces = (relay.Node, )
	@classmethod
	def get_node(cls, info, id):
		return InsuranceModel.objects.get(pk=id)

class DepartmentNode(DjangoObjectType):
	class Meta:
		model = DepartmentModel
		interfaces = (relay.Node, )
	@classmethod
	def get_node(cls, info, id):
		return DepartmentModel.objects.get(pk=id)
		
class CostCentreNode(DjangoObjectType):
	class Meta:
		model = CostCentreModel
		interfaces = (relay.Node, )
	@classmethod
	def get_node(cls, info, id):
		return CostCentreModel.objects.get(pk=id)

class BedNode(DjangoObjectType):
	class Meta:
		model = BedModel
		interfaces = (relay.Node, )
	@classmethod
	def get_node(cls, info, id):
		return BedModel.objects.get(pk=id)

class RoomNode(DjangoObjectType):
	class Meta:
		model = RoomModel
		interfaces = (relay.Node, )
	@classmethod
	def get_node(cls, info, id):
		return RoomModel.objects.get(pk=id)

class WardNode(DjangoObjectType):
	class Meta:
		model = WardModel
		interfaces = (relay.Node, )
	@classmethod
	def get_node(cls, info, id):
		return WardModel.objects.get(pk=id)

class RoomTypeNode(DjangoObjectType):
	class Meta:
		model = RoomTypeModel
		interfaces = (relay.Node, )
	@classmethod
	def get_node(cls, info, id):
		return RoomTypeModel.objects.get(pk=id)

class ProcedureNode(DjangoObjectType):
	class Meta:
		model = ProcedureModel
		interfaces = (relay.Node, )

class PatientProcedure(DjangoObjectType):
	class Meta:
		model = PatientProcedureModel
		interfaces = (relay.Node, )

class ProcedureCategoryNode(DjangoObjectType):
	class Meta:
		model = ProcedureCategoryModel
		interfaces = (relay.Node, )
		
class PatientProcedureNode(DjangoObjectType):
	class Meta:
		model = PatientProcedureModel
		interfaces = (relay.Node, )

class PatientProcedureNoteNode(DjangoObjectType):
	class Meta:
		model = PatientProcedureNoteModel
		interfaces = (relay.Node, )

class Query(graphene.ObjectType):
	users = graphene.List(User)
	patients = graphene.List(PatientDemographNode)
	insurances = graphene.List(InsuranceNode)
	insuranceSchemes = graphene.List(InsuranceSchemeNode)
	logAppointments = graphene.List(LogAppointmentNode)
	patientQueue = graphene.List(PatientQueue)
	departments = graphene.List(DepartmentNode)
	costCentre = graphene.List(CostCentreNode)
	rooms = graphene.List(RoomNode)
	wards = graphene.List(WardNode)
	roomTypes = graphene.List(RoomTypeNode)
	beds = graphene.List(BedNode)
	procedures = graphene.List(ProcedureNode)
	procedureCategories = graphene.List(ProcedureCategoryNode)
	patientProcedures = graphene.List(PatientProcedureNode)
	patientProcedureNotes = graphene.List(PatientProcedureNoteNode)

	@graphene.resolve_only_args
	def resolve_users(self):
		return UserModel.objects.all()[0:100]

	@graphene.resolve_only_args
	def resolve_patients(self):
		return PatientModel.objects.all()[0:100]

	@graphene.resolve_only_args
	def resolve_insurances(self):
		return InsuranceModel.objects.all()[0:100]

	@graphene.resolve_only_args
	def resolve_insuranceSchemes(self):
		return InsuranceSchemeModel.objects.all()[0:100]

	@graphene.resolve_only_args
	def resolve_logAppointments(self):
		return LogAppointmentModel.objects.all()[0:100]

	@graphene.resolve_only_args
	def resolve_patientQueue(self):
		return PatientQueueModel.objects.all()[0:100]

	@graphene.resolve_only_args
	def resolve_departments(self):
		return DepartmentModel.objects.all()[0:100]

	@graphene.resolve_only_args
	def resolve_costCentre(self):
		return CostCentreModel.objects.all()[0:100]

	@graphene.resolve_only_args
	def resolve_rooms(self):
		return RoomModel.objects.all()[0:100]

	@graphene.resolve_only_args
	def resolve_wards(self):
		return WardModel.objects.all()[0:100]

	@graphene.resolve_only_args
	def resolve_roomTypes(self):
		return RoomTypeModel.objects.all()[0:100]

	@graphene.resolve_only_args
	def resolve_beds(self):
		return BedModel.objects.all()[0:100]

	@graphene.resolve_only_args
	def resolve_procedures(self):
		return ProcedureModel.objects.all()[0:100]

	@graphene.resolve_only_args
	def resolve_procedureCategories(self):
		return ProcedureCategoryModel.objects.all()[0:100]	

	@graphene.resolve_only_args
	def resolve_patientProcedures(self):
		return PatientProcedureModel.objects.all()[0:100]

	@graphene.resolve_only_args
	def resolve_patientProcedureNotes(self):
		return PatientProcedureNoteModel.objects.all()[0:100]	

schema = graphene.Schema(query=Query)