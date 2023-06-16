subroutine add_2d_arrays(array, result, nrows, ncols)
  implicit none
  integer, intent(in), value :: nrows, ncols
  real(8), dimension(nrows, ncols), intent(in) :: array
  real(8), dimension(nrows), intent(out) :: result
  integer :: i, j

  do i = 1, nrows
    result(i) = 0.0
    do j = 1, ncols
      result(i) = result(i) + array(i, j)
    end do
  end do

end subroutine add_2d_arrays
